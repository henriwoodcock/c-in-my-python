import ctypes

def load_lib() -> ctypes.CDLL:
  lib = ctypes.cdll.LoadLibrary('build/src/libmagnitude.dylib')
  lib.Magnitude.restype = ctypes.c_float

  return lib

def load_array(array):
  c_array = (ctypes.c_float * len(array))(*array)

  return c_array

def test_cases(lib):
  test1_array = [3, 4]
  test1_array = load_array(test1_array)
  test1_result = lib.Magnitude(test1_array, 2);
  assert test1_result == 5.0

  test2_array = [1, 1, 1, 1];
  test2_array = load_array(test2_array)
  test2_result = lib.Magnitude(test2_array, 4);
  assert test2_result == 2.0

  print("ALL TESTS PASSED")

def main():
  lib = load_lib()
  test_cases(lib)

  return 0

if __name__ == "__main__":
  main()
