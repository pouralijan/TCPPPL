cmake_minimum_required(VERSION 3.14)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(PROJECTNAME TC++PL)
project(${PROJECTNAME})

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include_directories(. ../src)

set(SOURCE_LIST 
	./src/Main.cpp
	./src/Vector.cpp
	)

add_executable(${PROJECTNAME} ${SOURCE_LIST})

install(TARGETS ${PROJECTNAME} RUNTIME DESTINATION bin)
