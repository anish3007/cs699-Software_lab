#!/bin/bash

for file in *.*
do
    filename="${file%.*}"
    ext="${file##*.}"
    mv "$file" "$filename""hallo.$ext"
done
