#!/bin/bash

find . -mindepth 2 -type f | while read file; do
    # echo "$file"
    newname=${file:2}
    newname=${newname//\//_}
    cp "$file" ./"$newname"
done
