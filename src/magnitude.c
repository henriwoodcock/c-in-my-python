#include <math.h>

#include "magnitude.h"

float Magnitude(float arr [], int arr_len) {
  float magnitude = 0;

  for (int i = 0; i < arr_len; i++) {
    magnitude += arr[i] * arr[i];
  }

  magnitude = sqrt(magnitude);

  return magnitude;
}
