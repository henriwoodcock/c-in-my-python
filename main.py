import ctypes


def load_lib() -> ctypes.CDLL:
  lib = ctypes.cdll.LoadLibrary('build/src/libmy_c_lib.dylib')
  lib.Magnitude.restype = ctypes.c_float

  return lib


def load_array(array):
  c_array = (ctypes.c_float * len(array))(*array)

  return c_array


def magnitude_test_cases(lib):
  test1_array = [3, 4]
  test1_array = load_array(test1_array)
  test1_result = lib.Magnitude(test1_array, 2);
  assert test1_result == 5.0

  test2_array = [1, 1, 1, 1];
  test2_array = load_array(test2_array)
  test2_result = lib.Magnitude(test2_array, 4);
  assert test2_result == 2.0


def scalar_mult_test_cases(lib):
  test1_array = [3, 4]
  test1_array = load_array(test1_array)
  test1_scalar = ctypes.c_float(1.0)
  test1_expected = [3, 4]
  lib.ScalarMult(test1_scalar, test1_array, 2);
  for i in range(2):
    assert test1_array[i] == test1_expected[i]

  test2_array = [1, 1, 1, 1];
  test2_array = load_array(test2_array)
  test2_scalar = ctypes.c_float(2.0)
  test2_expected = [2, 2, 2, 2]
  lib.ScalarMult(test2_scalar, test2_array, 4);
  for i in range(4):
    assert test2_array[i] == test2_expected[i]


def vec_sum_test_cases(lib):
  test1_array1 = [3, 4]
  test1_array1 = load_array(test1_array1)
  test1_array2 = [1, 1]
  test1_array2 = load_array(test1_array2)
  test1_expected = [4, 5]
  lib.VecSum(test1_array1, test1_array2, 2);
  for i in range(2):
    assert test1_array1[i] == test1_expected[i]

  test2_array1 = [1, 1, 1, 1]
  test2_array1 = load_array(test2_array1)
  test2_array2 = [1, 2, 3, 4]
  test2_array2 = load_array(test2_array2)
  test2_expected = [2, 3, 4, 5]
  lib.VecSum(test2_array1, test2_array2, 4);
  for i in range(4):
    assert test2_array1[i] == test2_expected[i]


def main():
  lib = load_lib()
  magnitude_test_cases(lib)
  scalar_mult_test_cases(lib)
  vec_sum_test_cases(lib)

  print("ALL TESTS PASSED")

  return 0

if __name__ == "__main__":
  main()
