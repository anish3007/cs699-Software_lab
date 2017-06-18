#!/bin/bash

rm tab3
cat tab1>>tab4
cat tab2>>tab4
echo "files tab1 and tab2 merged into tab3"
sort -k $1 tab4>>tab3
rm tab4

