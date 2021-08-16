# test magnitude
add_executable(test_magnitude)

target_sources(test_magnitude PRIVATE
  ${CMAKE_CURRENT_LIST_DIR}/test_magnitude.c
)

target_include_directories(test_magnitude PUBLIC
  ${CMAKE_SOURCE_DIR}/include
)

target_link_libraries(test_magnitude PUBLIC my_c_lib)


# test scalar mult
add_executable(test_scalar_mult)

target_sources(test_scalar_mult PRIVATE
  ${CMAKE_CURRENT_LIST_DIR}/test_scalar_mult.c
)

target_include_directories(test_scalar_mult PUBLIC
  ${CMAKE_SOURCE_DIR}/include
)

target_link_libraries(test_scalar_mult PUBLIC my_c_lib)


# test vec sum
add_executable(test_vec_sum)

target_sources(test_vec_sum PRIVATE
  ${CMAKE_CURRENT_LIST_DIR}/test_vec_sum.c
)

target_include_directories(test_vec_sum PUBLIC
  ${CMAKE_SOURCE_DIR}/include
)

target_link_libraries(test_vec_sum PUBLIC my_c_lib)
