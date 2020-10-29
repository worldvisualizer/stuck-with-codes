cmake_minimum_required(VERSION 3.15)
project(json_reader VERSION 1.0.0 LANGUAGES CXX)
set(CMAKE_BUILD_TYPE Debug)
add_executable(json_reader read_map.cpp)

set(JSON_BuildTests OFF CACHE INTERNAL "")
add_subdirectory(nlohmann_json)
target_link_libraries(json_reader PRIVATE nlohmann_json::nlohmann_json)
