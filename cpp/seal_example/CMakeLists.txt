cmake_minimum_required(VERSION 3.12)
project(desilo VERSION 1.0.0 LANGUAGES CXX)

# Enable testing, but we want to show the output from google test when executing from console, so we
# add our own target. Execute with for instance `make check`.
enable_testing()
add_custom_target(check COMMAND GTEST_COLOR=1 ${CMAKE_CTEST_COMMAND} --verbose)

# Retrieve the standard GNU installation paths
include(GNUInstallDirs)

# Import the "download_project" function for downloading dependencies during the configure phase.
include(contrib/cmake-downloadProject/DownloadProject.cmake)

# Download microsoft/SEAL dependency during CMake configure time
download_project(
    PROJ                seal
    GIT_REPOSITORY      https://github.com/microsoft/SEAL.git
    GIT_TAG             master
    GIT_SHALLOW         true
    ${UPDATE_DISCONNECTED_IF_AVAILABLE}
)

download_project(
    PROJ                googletest
    GIT_REPOSITORY      https://github.com/google/googletest.git
    GIT_TAG             release-1.8.0
    GIT_SHALLOW         true
    ${UPDATE_DISCONNECTED_IF_AVAILABLE}
)

# Prevent gtest from overriding the parent project's compiler/linker
# when building with Microsoft Visual Studio
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)

# Add seal directly to our build. 
# TODO: find out what this means - This defines the gtest and gtest_main targets.
add_subdirectory(${seal_SOURCE_DIR}
                 ${seal_BINARY_DIR}
                 EXCLUDE_FROM_ALL)
add_subdirectory(${googletest_SOURCE_DIR}
                 ${googletest_BINARY_DIR}
                 EXCLUDE_FROM_ALL)
add_subdirectory(crypto)
add_subdirectory(evaluators)
add_subdirectory(desilo)
