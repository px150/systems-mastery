#define _POSIX_C_SOURCE 200809L

#include <stdint.h>
#include <stdio.h>
#include <time.h>

#define N 400000000ULL

static double elapsed_seconds(struct timespec start,
                              struct timespec end)
{
    return (double)(end.tv_sec - start.tv_sec) +
           (double)(end.tv_nsec - start.tv_nsec) / 1e9;
}

// __attribute__((noinline))
// uint64_t dependent(uint64_t x)
// {
//     for (uint64_t i = 0; i < N/4; i++) {
//         x = x * 3 + 1;
//         x = x * 3 + 1;
//         x = x * 3 + 1;
//         x = x * 3 + 1;
//     }

//     return x;
// }

// __attribute__((noinline))
// uint64_t independent(uint64_t x)
// {
//     uint64_t a = x;
//     uint64_t b = x + 1;
//     uint64_t c = x + 2;
//     uint64_t d = x + 3;

//     for (uint64_t i = 0; i < N / 4; i++) {
//         a = a * 3 + 1;
//         b = b * 3 + 1;
//         c = c * 3 + 1;
//         d = d * 3 + 1;
//     }

//     return a ^ b ^ c ^ d;
// }

__attribute__((noinline))
uint64_t dependent(uint64_t x)
{
    for (uint64_t i = 0; i < N / 4; i++) {
        __asm__ volatile (
            "lea 1(%0,%0,2), %0\n\t"
            "lea 1(%0,%0,2), %0\n\t"
            "lea 1(%0,%0,2), %0\n\t"
            "lea 1(%0,%0,2), %0"
            : "+r"(x)
        );
    }

    return x;
}

__attribute__((noinline))
uint64_t independent(uint64_t x)
{
    uint64_t a = x;
    uint64_t b = x + 1;
    uint64_t c = x + 2;
    uint64_t d = x + 3;

    for (uint64_t i = 0; i < N / 4; i++) {
        __asm__ volatile (
            "lea 1(%0,%0,2), %0\n\t"
            "lea 1(%1,%1,2), %1\n\t"
            "lea 1(%2,%2,2), %2\n\t"
            "lea 1(%3,%3,2), %3"
            : "+r"(a), "+r"(b), "+r"(c), "+r"(d)
        );
    }

    return a ^ b ^ c ^ d;
}

int main(void)
{
    struct timespec start, end;

    clock_gettime(CLOCK_MONOTONIC, &start);
    uint64_t result_a = dependent(1);
    clock_gettime(CLOCK_MONOTONIC, &end);

    printf("Dependent:   %.6f s (result: %llu)\n",
           elapsed_seconds(start, end),
           (unsigned long long)result_a);

    clock_gettime(CLOCK_MONOTONIC, &start);
    uint64_t result_b = independent(1);
    clock_gettime(CLOCK_MONOTONIC, &end);

    printf("Independent: %.6f s (result: %llu)\n",
           elapsed_seconds(start, end),
           (unsigned long long)result_b);

    return 0;
}
