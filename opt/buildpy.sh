#!/bin/bash


pushd .


#tar zxvf pybind11-2.6.2.tar.gz
#cd pybind11-2.6.2
#cmake -DPYBIND11_NOPYTHON=ON  -DPYBIND11_TEST=OFF  .
#cd ..

#tar zxvf protobuf-cpp-3.17.3.tar.gz
#cd protobuf-3.17.3
#./configure  --disable-shared  --prefix=`pwd`/../../bin/protobuf
#make -j4
#make install
#cd ..



#export CPPFLAGS=" -Wno-error=coverage-mismatch"


#NOTICE  ubuntu : bz2-devel  xz-dev libffi-dev  libgdbm-dev tk tk-dev  libffi-dev
#        centos : zlib zlib-devel bzip2-devel  xz-devel  libffi-devel  uuid-devel  tcl-devel  tk-devel  readline-devel gdbm-devel
#tar zxvf Python-3.9.10.tgz

cd  Python-3.13.0a6

SSLPATH=`pwd`/../../bin/openssl

export CFLAGS="-I${SSLPATH}/include -I./Include/internal/"
export LDFLAGS="-L${SSLPATH}/lib"
export LD_LIBRARY_PATH=${SSLPATH}/lib
CFLAGS="-I${SSLPATH}/include"
LDFLAGS="-L${SSLPATH}/lib"



echo $CFLAGS
echo $LDFLAGS
#./configure    --with-system-ffi  --prefix=`pwd`/../../bin/python  --enable-optimizations   --with-lto --enable-shared
#./configure   --with-openssl=`pwd`/../../bin/openssl   --prefix=`pwd`/../../bin/python  --enable-optimizations   --with-lto --enable-shared
PYTHON_GIL=0
export PYTHON_GIL=0

./configure     --prefix=`pwd`/../../bin/python  --enable-optimizations   --with-lto --disable-gil    --disable-test-modules 

#./configure    --with-system-ffi  --prefix=`pwd`/../../bin/python  --enable-optimizations   --with-lto --enable-shared
#./configure    --with-system-ffi  --prefix=`pwd`/../../bin/python  --enable-optimizations   --with-lto  --disable-shared
make -j8
make install
cd ..

popd

