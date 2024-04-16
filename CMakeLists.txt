cmake_minimum_required(VERSION 3.13)
project (mtpy VERSION 0.6 )
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)





set(CMD_CXXFLAGS "pkg-config" "--cflags" "./bin/python/lib/pkgconfig/python3-embed.pc")
set(CMD_LDFLAGS "pkg-config" "--libs" "--static"  "./bin/python/lib/pkgconfig/python3-embed.pc")




execute_process(COMMAND   ${CMD_CXXFLAGS}
                WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
                OUTPUT_VARIABLE   SEASTAR_CXX_FLAGS)

string(STRIP "${PYTHON_CXX_FLAGS}" PYTHON_CXX_FLAGS)


execute_process(COMMAND  ${CMD_LDFLAGS}
                WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
                OUTPUT_VARIABLE   PYTHON_LD_FLAGS)

string(STRIP "${PYTHON_LD_FLAGS}" PYTHON_LD_FLAGS)




if(APPLE)
    set(CMAKE_MACOSX_RPATH 1)
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pthread -g  -Wall -Wno-unused-function -Wl,-rpath,. -Wl,-rpath,bin  ")
elseif(UNIX)
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -pthread  -O2 -g  -Wno-unused-function  -Wno-deprecated-declarations -Wl,-rpath,. -Wl,-rpath,bin  -Wl,-rpath,bin/lib/x86_64-linux-gnu"  )
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${PYTHON_CXX_FLAGS}  -Wall -pthread -O2  -g -Wno-unused-function  -Wno-deprecated-declarations -Wl,-rpath,. -Wl,-rpath,bin     "  )
elseif(WIN32)
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ")
endif()

message(STATUS ${PYTHON_CXX_FLAGS})
message(STATUS "===============link flags ===============")
message(STATUS ${PYTHON_LD_FLAGS})
message(STATUS "===============end link flags ===============")

add_subdirectory(opt/pybind11-2.12.0)

include_directories(./bin/python/include/python3.13t/)
include_directories(opt/pybind11-2.12.0/include)

link_directories(./bin/python/lib) 

add_executable(mtengine src/mtengine.cpp)
target_link_libraries(mtengine PRIVATE pybind11::embed  python3.13t  dl )
