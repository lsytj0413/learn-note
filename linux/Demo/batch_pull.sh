#!/bin/bash

PWD=$(pwd)
if [ -n "$1" ]; then
    PWD=$1
fi

if [[ ! (-d "$PWD") ]]; then
    echo $PWD must be a valid directory pathname.
    exit 1
fi

echo batch pull on directory: $PWD

DIRS=$(ls)
for dirname in $DIRS; do
    dirpath="$PWD/$dirname"
    if [[ -d "$dirpath" ]]; then
        echo "git pull in directory: $dirpath"
        cd $dirpath
        git pull
        cd ..
    fi
done

echo batch pull done.
