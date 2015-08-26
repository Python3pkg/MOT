#ifndef SPREAD_WEIGHTS_%(MEMSPACE)r_H
#define SPREAD_WEIGHTS_%(MEMSPACE)r_H

/**
 * Author = Robbert Harms
 * Date = 2014-02-01
 * License = LGPL v3
 * Maintainer = Robbert Harms
 * Email = robbert.harms@maastrichtuniversity.nl
 */

/**
 * Calculate the model weights when one more weight is needed than that is optimized at the moment.
 * Input:
 *  - x: a double array with enough space for all of the elements, and with the first n-1 initialized with the
 *        current weights
 *  - n: the total number of elements in the array x
 * Output: the same array but then with all the elements set to their correct values
 *
 * Examples:
 * x = [0.8, 0.5, 0]
 * n = 3
 * spread_weights(x,n, 1.0)
 * x = [0.615, 0.384, 0]
 *
 * x = [0.2, 0.2, 0]
 * n = 3
 * spread_weights(x,n, 1.0)
 * x = [0.2, 0.2, 0.6]
 */

void spread_weights_%(MEMSPACE)r(const %(MEMSPACE)r double* const x, const int n);

#endif // SPREAD_WEIGHTS_%(MEMSPACE)s_H