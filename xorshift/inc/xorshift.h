#ifndef XORSHIFT_H
#define XORSHIFT_H


#include <stdint.h>


/*
 * xorshift128 state structure.
 *
 * Represents the internal 128-bit state of the generator.
 * The all-zero state is invalid.
 */
typedef struct {
    uint32_t x;
    uint32_t y;
    uint32_t z;
    uint32_t w;
} xorshift_t;


/*
 * Initialize the xorshift generator state.
 *
 * The supplied state must not be all-zero.
 */
void xorshift_init(const xorshift_t *xorshift);


/*
 * Generate a pseudorandom number.
 *
 * Returns a 16-bit value derived from a 128-bit xorshift generator
 * with nonlinear output scrambling.
 */
uint32_t xorshift_rand(void);


#endif /* XORSHIFT_H */
