#include <assert.h>
#include <stdio.h>

#include "scalar_mult.h"

int main() {
  float test1_array[] = {3, 4};
  float test1_expected[] = {3, 4};
  ScalarMult(1, test1_array, 2);
  for (int i = 0; i < 2; i++) {
    assert (test1_array[i] == test1_expected[i]);
  }

  float test2_array[] = {1, 1, 1, 1};
  float test2_expected[] = {2, 2, 2, 2};
  ScalarMult(2, test2_array, 4);
  for (int i = 0; i < 4; i++) {
    assert (test2_array[i] == test2_expected[i]);
  }

  printf("ALL TESTS PASSED\n");
  return 0;
}
