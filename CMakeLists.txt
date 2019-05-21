cmake_minimum_required(VERSION 3.14)

set(COMPILER "GCC" CACHE STRING "GCC")
message("Compiler parameter is set to ${COMPILER}.")
if(COMPILER STREQUAL "CLANG")
  set(CMAKE_C_COMPILER "clang")
  set(CMAKE_CXX_COMPILER "clang++")
  message("Compiler is set to ${COMPILER} succssfully.")
endif(COMPILER STREQUAL "CLANG")

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(PROJECTNAME TC++PL)
project(${PROJECTNAME})

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include_directories(../src)

set(SOURCE_LIST 
	./src/Main.cpp
	./src/Vector.cpp
)

add_executable(${PROJECTNAME} ${SOURCE_LIST})

install(TARGETS ${PROJECTNAME} RUNTIME DESTINATION bin)
