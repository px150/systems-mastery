#define _POSIX_C_SOURCE 200809L

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>

/*
 * Memory hierarchy experiments.
 *
 * Experiment 1 — Access pattern
 * --------------------------------
 * Compare sequential access with strided access over a data set that is
 * intentionally much larger than the CPU caches.
 *
 * The goal is to observe how different memory access patterns affect the
 * average cost per access. Sequential traversal can make effective use of
 * spatial locality: when a cache line is fetched, several adjacent integers
 * can be consumed before another line is needed.
 *
 * With STRIDE = 16 and 4-byte ints, consecutive strided accesses are
 * 64 bytes apart, matching the cache-line size observed on the test machine.
 * This greatly reduces the useful data consumed from each fetched cache line.
 *
 * The benchmark performs approximately the same total number of accesses in
 * both cases so that ns/access can be meaningfully compared.
 *
 *
 * Experiment 2 — Working-set size
 * --------------------------------
 * Repeatedly traverse data sets of different sizes while keeping the total
 * amount of data read approximately constant.
 *
 * The goal is to observe how the average access cost changes as the active
 * working set grows beyond the capacity of progressively larger cache levels.
 *
 * Cache capacities observed on the test machine:
 *
 *     L1d: ~48 KiB per instance
 *     L2:  ~1.25 MiB per instance
 *     L3:  ~24 MiB
 *
 * The tested working sets intentionally fall below or above these boundaries.
 */

#define ELEMENTS (64 * 1024 * 1024)  /* ~256 MiB when sizeof(int) == 4 */
#define STRIDE 16                    /* 16 ints * 4 B = 64 B */
#define REPEATS 10

/*
 * Total amount of useful data read for each working-set experiment.
 *
 * Keeping this approximately constant makes results across different
 * working-set sizes more comparable.
 */
#define TOTAL_BYTES (1ULL * 1024 * 1024 * 1024)  /* 1 GiB */

/*
 * Return the elapsed time between two monotonic-clock measurements.
 */
static double elapsed_seconds(struct timespec start, struct timespec end)
{
    return (end.tv_sec - start.tv_sec)
         + (end.tv_nsec - start.tv_nsec) / 1e9;
}

/*
 * Repeatedly traverse the first working_set_elements elements of data.
 *
 * Small working sets can remain in nearby cache levels between traversals,
 * while larger working sets progressively exceed their capacity.
 *
 * The number of repetitions is adjusted according to the working-set size
 * so that every experiment reads approximately TOTAL_BYTES overall.
 *
 * The returned value is the average number of nanoseconds per access.
 */
static double benchmark_working_set(
    int *data,
    size_t working_set_elements,
    volatile uint64_t *sum)
{
    uint64_t working_set_bytes =
        (uint64_t)working_set_elements * sizeof(int);

    uint64_t repeats = TOTAL_BYTES / working_set_bytes;

    /*
     * Ensure that even a working set larger than TOTAL_BYTES would still
     * be traversed at least once.
     */
    if (repeats == 0) {
        repeats = 1;
    }

    uint64_t accesses =
        (uint64_t)working_set_elements * repeats;

    struct timespec start, end;

    clock_gettime(CLOCK_MONOTONIC, &start);

    for (uint64_t r = 0; r < repeats; r++) {
        for (size_t i = 0; i < working_set_elements; i++) {
            *sum += data[i];
        }
    }

    clock_gettime(CLOCK_MONOTONIC, &end);

    double seconds = elapsed_seconds(start, end);

    return seconds * 1e9 / accesses;
}

int main(void)
{
    int *data = malloc(ELEMENTS * sizeof(int));

    if (data == NULL) {
        fprintf(stderr, "Allocation failed\n");
        return 1;
    }

    /*
     * Initialize the entire allocation before measuring it.
     * Initialization is deliberately excluded from the benchmarks.
     */
    for (size_t i = 0; i < ELEMENTS; i++) {
        data[i] = (int)i;
    }

    /*
     * Make the accumulated result observable so that the compiler cannot
     * simply eliminate the memory-reading loops as unused work.
     */
    volatile uint64_t sum = 0;
    struct timespec start, end;

    /*
     * ================================================================
     * Experiment 1: sequential vs strided access
     * ================================================================
     */

    /*
     * Sequential access.
     *
     * Adjacent ints are read consecutively, allowing data brought in by one
     * cache-line fetch to be reused by several following accesses.
     */
    clock_gettime(CLOCK_MONOTONIC, &start);

    for (int r = 0; r < REPEATS; r++) {
        for (size_t i = 0; i < ELEMENTS; i++) {
            sum += data[i];
        }
    }

    clock_gettime(CLOCK_MONOTONIC, &end);

    double sequential_time = elapsed_seconds(start, end);
    uint64_t sequential_accesses =
        (uint64_t)ELEMENTS * REPEATS;

    /*
     * Strided access.
     *
     * Only every STRIDE-th element is read. With the values used here,
     * successive accesses are one cache line apart.
     *
     * The outer loop runs STRIDE times more often to keep the total number
     * of memory accesses approximately equal to the sequential experiment.
     * This prevents the strided case from appearing faster merely because
     * it performs fewer reads.
     */
    clock_gettime(CLOCK_MONOTONIC, &start);

    for (int r = 0; r < REPEATS * STRIDE; r++) {
        for (size_t i = 0; i < ELEMENTS; i += STRIDE) {
            sum += data[i];
        }
    }

    clock_gettime(CLOCK_MONOTONIC, &end);

    double strided_time = elapsed_seconds(start, end);
    uint64_t strided_accesses =
        ((uint64_t)ELEMENTS / STRIDE) * REPEATS * STRIDE;

    /*
     * Normalize total execution time by the number of accesses.
     *
     * ns/access is a throughput-oriented average for this benchmark. It must
     * not be interpreted as the latency of one individual RAM access.
     */
    printf("=== Access pattern ===\n");

    printf("Sequential: %.3f s, %.2f ns/access\n",
           sequential_time,
           sequential_time * 1e9 / sequential_accesses);

    printf("Stride 16:  %.3f s, %.2f ns/access\n",
           strided_time,
           strided_time * 1e9 / strided_accesses);

    /*
     * ================================================================
     * Experiment 2: working-set size
     * ================================================================
     *
     * These sizes intentionally cross the cache capacities observed on
     * the test machine:
     *
     *     16 KiB   < L1d
     *     256 KiB  > L1d, < L2
     *     2 MiB    > L2,  < L3
     *     32 MiB   > L3
     *     100 MiB  > L3
     *
     * These comparisons are intentionally approximate: cache capacity alone
     * does not determine the exact performance of a real machine.
     */
    const size_t working_sets[] = {
        16ULL * 1024,
        256ULL * 1024,
        2ULL * 1024 * 1024,
        32ULL * 1024 * 1024,
        100ULL * 1024 * 1024
    };

    const char *labels[] = {
        "16 KiB",
        "256 KiB",
        "2 MiB",
        "32 MiB",
        "100 MiB"
    };

    const size_t working_set_count =
        sizeof(working_sets) / sizeof(working_sets[0]);

    printf("\n=== Working set ===\n");

    for (size_t i = 0; i < working_set_count; i++) {
        /*
         * working_sets stores sizes in bytes. Convert each size into the
         * corresponding number of int elements before running the benchmark.
         */
        size_t elements =
            working_sets[i] / sizeof(int);

        double ns_per_access =
            benchmark_working_set(data, elements, &sum);

        printf("%-7s: %.2f ns/access\n",
               labels[i],
               ns_per_access);
    }

    /*
     * The actual value is irrelevant. Printing it simply makes the result
     * observable outside the benchmark.
     */
    printf("\nIgnore: %llu\n",
           (unsigned long long)sum);

    free(data);

    return 0;
}