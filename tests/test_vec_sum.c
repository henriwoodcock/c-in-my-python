#include <assert.h>
#include <stdio.h>

#include "vec_sum.h"

int main() {
  float test1_array1[] = {3, 4};
  float test1_array2[] = {1, 1};
  float test1_expected[] = {4, 5};
  VecSum(test1_array1, test1_array2, 2);
  for (int i = 0; i < 2; i++) {
    assert (test1_array1[i] == test1_expected[i]);
  }

  float test2_array1[] = {1, 1, 1, 1};
  float test2_array2[] = {1, 2, 3, 4};
  float test2_expected[] = {2, 3, 4, 5};
  VecSum(test2_array1, test2_array2, 4);
  for (int i = 0; i < 4; i++) {
    assert (test2_array1[i] == test2_expected[i]);
  }

  printf("ALL TESTS PASSED\n");
  return 0;
}
