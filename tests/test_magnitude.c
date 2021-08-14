#include <assert.h>
#include <stdio.h>

#include "magnitude.h"

int main() {
  float test1_array[] = {3, 4};
  float test1_result = Magnitude(test1_array, 2);
  assert (test1_result == 5.0f);

  float test2_array[] = {1, 1, 1, 1};
  float test2_result = Magnitude(test2_array, 4);
  assert (test2_result == 2.0f);

  printf("ALL TESTS PASSED\n");
  return 0;
}
