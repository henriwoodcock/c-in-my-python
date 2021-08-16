add_library(my_c_lib SHARED
  ${CMAKE_CURRENT_LIST_DIR}/magnitude.c
  ${CMAKE_CURRENT_LIST_DIR}/scalar_mult.c
  ${CMAKE_CURRENT_LIST_DIR}/vec_sum.c
)

target_include_directories(my_c_lib PUBLIC
  ${CMAKE_SOURCE_DIR}/include
)
