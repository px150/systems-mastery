#include <stdint.h>
#include <stdio.h>

int main(void) {
    uint8_t value = 255;

    printf("before: %u\n", value);

    value = value + 1;

    printf("after:  %u\n", value);

    return 0;
}