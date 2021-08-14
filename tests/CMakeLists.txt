add_executable(test_magnitude)

target_sources(test_magnitude PRIVATE
  ${CMAKE_CURRENT_LIST_DIR}/test_magnitude.c
)

target_include_directories(test_magnitude PUBLIC
  ${CMAKE_SOURCE_DIR}/include
)

target_link_libraries(test_magnitude PUBLIC magnitude)
