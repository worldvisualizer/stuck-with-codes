
# Commenting in CMake
# mkdir build && cd build && cmake .. && make -j

# Creates OS-dependent Makefile, and then Makefile is run.
# CMake is essentially a cross-platform, open-source build system. 
# Basically, any C++/C project becomes package/library of your choice through CMake

# Significance: build process becomes independent of OS and Compiler
# Works with: Makefiles in Unix, Projects/Workspaces in Windows MSVC

cmake_minimum_required(VERSION 2.8)

cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

project (learncmake C)

# set the project source directory
set(LEARN_CMAKE_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR})
set(LEARN_CMAKE_BINARY_DIR ${CMAKE_CURRENT_BINARY_DIR})

# useful to set up the current version of the code in the build system
set(LEARN_CMAKE_VERSION_MAJOR 1)
set(LEARN_CMAKE_VERSION_MINOR 0)
set(LEARN_CMAKE_VERSION_PATCH 0)

# send the variables to source code header
# note: PROJECT_SOURCE_DIR is prob. not set
configure_file(
    "${PROJECT_SOURCE_DIR}/TUtorialConfig.h.in"
    "${PROJECT_BINARY_DIR}/TUtorialConfig.h"
)

# include directories
include_directories(include)

# if there are additional libraries installed, include path here
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/CMake/modules")

if (CONDITION)
    # messages

    # incidental information
    message(STATUS "My message")
    # CMake warning, continue processing
    message(WARNING "My message")
    # CMake warning (dev), continue processing
    message(AUTHOR_WARNING "My message")
    # CMake error, continue processing, but skip generation
    message(SEND_ERROR "My message")
    # CMake error, stop processing and generation
    message(FATAL_ERROR "My message")

endif()

if (CONDITION)
elseif(CONDITION)
else(CONDITION) # TODO: why is there a condition?
endif(CONDITION) # TODO: why is there a condition?

# loops
foreach (loop_var arg1 arg2 ...)
    COMMAND1(ARGS ...)
    COMMAND2(ARGS ...)
endforeach (loop_var) # again, why is there a variable referenced?

foreach (loop_var RANGE total)
foreach (loop_var RANGE start stop [step])
foreach (loop_var IN [LISTS [list1 [...]]])
foreach (loop_var IN [ITEMS [item1 [...]]])

while (condition)
    COMMAND1(ARGS ...)
    COMMAND2(ARGS ...)
endwhile (condition)

# logic operations
if (FALSE AND (FALSE OR TRUE))
    message("Don't display!")
endif()

# set a regular, cache, or environment variable to a given value
# if the PARENT_SCOPE is given, the variable will be set in the scope above the current scope.
# how to reference variables inside quoted and unquoted arguments?
# a variable reference is replaced by either the variable value or by the empty string if the variable is not set.

# Lists 
# setup the list of source files
set(LEARN_CMAKE_SOURCES src/main.c src/imagem.c src/pather.c)

# calls the compiler
add_executable(${PROJECT_NAME} ${LEARN_CMAKE_SOURCES})

# link the libraries
target_link_libraries(${PROJECT_NAME} ${LIBS} m)

# compiler condition (gcc; g++)
if ("${CMAKE_C_COMPILER_ID}" STREQUAL "GNU")
    message(STATUS "Setting the flags for ${CMAKE_C_COMPILER_ID} compiler")
    add_definitions(--std=c99)
endif()

# check for OS
if (UNIX)
    set(LEARN_CMAKE_DEFINITIONS
	"${LEARN_CMAKE_DEFINITIONS} -Wall -Wextra -Werror -Wno-deprecated-declarations -Wno-unused-parameter -Wno-comment")
endif()

# Helpful next step is...
# https://cliutils.gitlab.io/modern-cmake/
