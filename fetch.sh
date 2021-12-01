#!/usr/bin/env sh

# usage : 
# fetch.sh $DAY

if test -z $@; then
    echo "Argument required"

else
    SESSION=$(cat session.txt)
    d="$1"
    dd=$(echo $1 | sed 's/^0*//')
    mkdir -p day_$1_cpp
    touch day_$1_cpp/prog.cpp
    curl "https://adventofcode.com/2020/day/$dd/input" --cookie "session=$SESSION" > "day_$1_cpp/input.txt"
fi
