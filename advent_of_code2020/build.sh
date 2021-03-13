#!/usr/bin/env sh

# usage:
# build.sh day

if test -z $@; then
    echo "Argument required"
else
    # echo "Compilling"
    #id = $1
    g++ -Wall -Wextra -std=c++17 ./day_$1_cpp/prog.cpp && time ./day_$1_cpp/prog.out

fi
