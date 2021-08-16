#include <math.h>

#include "scalar_mult.h"

void ScalarMult(float scalar, float *arr, int arr_len) {
  for (int i = 0; i < arr_len; i++) {
    arr[i] = arr[i] * scalar;
  }
}
