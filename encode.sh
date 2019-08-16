#!/bin/sh

echo "Welcome to File Encoder~"
echo "Choose encode mode (Type number)"
echo "1) single file"
echo "2) whole folder (only encode one type of file)"
read mode

echo "What type of file do you want to encode? (Type number)"
echo "1) .py"
echo "2) .pkl"
echo "3) .h5"
read fileType

echo "What platform do you use? (Type number)"
echo "1) windows (.pyd)"
echo "2) linux (.so)"
read platform

timestamp=$(date +%Y%m%d%H%M%S)

if [[ $platform = "1" ]]; then #.pyd
    platform="pyd"
elif [[ $platform = "2" ]]; then #.so
    platform="so"
fi

if [[ $mode = "1" ]]; then #single file
    echo "Please type the full file path:"
    read filePath
    fileName="${filePath##*/}"
    fileName="${fileName%.*}"

    if [[ $fileType = "1" ]]; then #.py
        cp $filePath .
    elif [[ $fileType = "2" ]]; then #.pkl
        python encode_pkl.py $filePath $fileName
    elif [[ $fileType = "3" ]]; then #.h5
        python encode_h5.py $filePath $fileName
    fi

    python setup.py $fileName build_ext --inplace
    rm "$fileName".py
    rm "$fileName".c
    mv "$fileName".*."$platform" "$fileName"."$platform"
    mkdir -p output"$timestamp"
    mv "$fileName"."$platform" output"$timestamp"
    echo Ouput: "$fileName"."$platform"

elif [[ $mode = "2" ]]; then #whole folder
    echo "Please type the full folder path:"
    read folderPath

    for filePath in $folderPath/*; do
        full_fileName=$(basename -- "$filePath")
        fileName="${full_fileName%.*}"
        extension="${full_fileName##*.}"
        if [[ $fileType = "1" && $extension = "py" ]]; then
            cp $filePath .
        elif [[ $fileType = "2" && $extension = "pkl" ]]; then
            python encode_pkl.py $filePath $fileName
        elif [[ $fileType = "3" && $extension = "h5" ]]; then #.h5
            python encode_h5.py $filePath $fileName
        fi

        python setup.py $fileName build_ext --inplace
        rm "$fileName".py
        rm "$fileName".c
        mv "$fileName".*."$platform" "$fileName"."$platform"
        mkdir -p output"$timestamp"
        mv "$fileName"."$platform" output"$timestamp"
        echo Ouput: "$fileName"."$platform"
    done
fi
