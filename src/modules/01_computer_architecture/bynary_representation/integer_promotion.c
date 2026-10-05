#include <stdint.h>
#include <stdio.h>

int main(void) {
    uint8_t x = 255;

    int a = x + 1;
    uint8_t b = x + 1;

    printf("a = %d\n", a);
    printf("b = %u\n", b);

    return 0;
}