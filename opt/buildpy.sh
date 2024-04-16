#!/bin/bash


pushd .


#PYTHON_GIL=0
export PYTHON_GIL=0

./configure     --prefix=`pwd`/../../bin/python  --enable-optimizations   --with-lto --disable-gil    --disable-test-modules 

make -j8
make install
cd ..

popd

