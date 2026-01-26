/*
 * xorshift128* PRNG
 *
 * This implementation is based on George Marsaglia's xorshift generators:
 *
 *   G. Marsaglia, "Xorshift RNGs",
 *   Journal of Statistical Software, Vol. 8, Issue 14, 2003.
 *
 * The generator maintains a 128-bit internal state and updates it using
 * XOR and shift operations, which form a linear recurrence over GF(2).
 *
 * A nonlinear output transformation (multiplication modulo 2^32) is applied
 * to improve statistical properties and break linearity in the output.
 *
 * IMPORTANT:
 *   - This generator is NOT cryptographically secure.
 *   - The internal state transition is linear and predictable.
 *   - Suitable for simulation and Monte Carlo methods only.
 */


#include "xorshift.h"
#include <stddef.h>


/*
 * Internal generator state.
 *
 * The state consists of four 32-bit words, forming a 128-bit state vector: S = (x,y,z,w) ∈ GF(2)^128
 *
 * The all-zero state is forbidden, as it is a fixed point of the recurrence.
 */
static xorshift_t state;


/*
 * Initialize the xorshift generator state.
 *
 * Parameters:
 *   xorshift  - pointer to a user-supplied seed structure
 *
 * The seed MUST NOT be the all-zero vector. If all components are zero,
 * the generator will remain stuck at zero forever.
 *
 * This function performs no scrambling; the caller is responsible for
 * providing a valid, nonzero seed.
 */
void xorshift_init(const xorshift_t *xorshift)
{   

    // must not be all-zero
    state.x = xorshift->x;
    state.y = xorshift->y;
    state.z = xorshift->z;
    state.w = xorshift->w;
    
    return;
}



/*
 * Generate the next pseudorandom number.
 *
 * <https://www.jstatsoft.org/index.php/jss/article/view/v008i14/916>
 * 
 * 
 * Theory:
 *   The state update implements a linear transformation:
 *
 *     S_{n+1} = A · S_n
 *
 *   where A is a 128×128 binary matrix over GF(2). The parameters used
 *   here correspond to a maximal-period xorshift128 generator with
 *   period 2^128 − 1.
 *
 *   The shifts (15, 21, 4) are chosen so that the characteristic polynomial
 *   of A is primitive.
 *
 * Output transformation:
 *   The raw xorshift output is multiplied by an odd constant modulo 2^32.
 *   This introduces carry propagation and breaks linearity over GF(2),
 *   significantly improving statistical behavior.
 *
 * Return value:
 *   A 16-bit pseudorandom value derived from the high bits of the scrambled
 *   output.
 */
uint32_t xorshift_rand()
{   
    // (a,b,c) = ()

    uint32_t temp = (state.x ^ (state.x << 15));
    
    state.x = state.y;
    state.y = state.z;
    state.z = state.w;

    state.w = (state.w ^ (state.w >> 21)) ^ (temp ^ (temp >> 4));

    // breaks linearity
    return (state.w * 0x58FEF1D1) >> 16;
}
