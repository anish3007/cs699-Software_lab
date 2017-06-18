#!/bin/bash

FILES="
fibindex.py \
matmult.py \
binsearch.py \
transpose.py \
strings.py \
prepare-upload.sh \
"

if [ -d forupload ]; then
	echo "Directory forupload already exists; delete or move and rerun"
	exit 1
fi

mkdir forupload
allfilesfound=1
for f in $FILES
do
	if [ ! -f "$f" ]; then
		echo "File $f not found; an empty file must be included even if question not attempted"
		allfilesfound=0
	fi
done

if [ $allfilesfound -eq 0 ]; then
	exit 2
fi

for f in $FILES
do
	cp $f forupload
done

tar zcvf forupload.tgz forupload

echo "forupload.tgz is ready for upload"

