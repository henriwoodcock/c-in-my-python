add_library(magnitude SHARED
  ${CMAKE_CURRENT_LIST_DIR}/magnitude.c
)

target_include_directories(magnitude PUBLIC
  ${CMAKE_SOURCE_DIR}/include
)
