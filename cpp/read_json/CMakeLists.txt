cmake_minimum_required(VERSION 3.15)
project(json_reader VERSION 1.0.0 LANGUAGES CXX)
add_executable(json_reader read_json.cpp)

set(JSON_BuildTests OFF CACHE INTERNAL "")
add_subdirectory(nlohmann_json)
target_link_libraries(json_reader PRIVATE nlohmann_json::nlohmann_json)
