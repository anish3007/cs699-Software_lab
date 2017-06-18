#!/bin/bash

cat $1>>concatfile1.txt
cat $2>>concatfile1.txt
echo "$1 and $2 copied to a third file concatfile1.txt"
