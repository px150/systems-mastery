#include <stdint.h>
#include <stdio.h>

int main(void) {
    uint16_t value = 0x1234;
    uint8_t *bytes = (uint8_t *)&value;

    printf("value:   0x%04X\n", value);
    printf("byte[0]: 0x%02X\n", bytes[0]);
    printf("byte[1]: 0x%02X\n", bytes[1]);

    return 0;
}