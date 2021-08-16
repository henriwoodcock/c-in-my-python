#include "vec_sum.h"

void VecSum(float *arr1, float *arr2, int arr_len) {
  for (int i = 0; i < arr_len; i++) {
    arr1[i] += arr2[i];
  }
}
