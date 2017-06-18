#!/bin/bash

for file in *.$1
do
    filename="${file%.*}"
    convert "$filename.$1" "$filename.$2"
done    
