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

if [[ $mode = "1" ]]; then #single file
    echo "Please type the full file path:"
    read filePath
    fileName="${filePath##*/}"
    fileName="${fileName%.*}"

    if [[ $fileType = "2" ]]; then #.pkl
        python3 encode_pkl.py $filePath $fileName
    elif [[ $fileType = "3" ]]; then #.h5
        python3 encode_h5.py $filePath $fileName
    fi

    python3 setup.py $fileName build_ext --inplace
    if [[ $fileType != "1" ]]; then #.py
        rm "$fileName".py
    fi
    rm "$fileName".c
    mv "$fileName".*.so "$fileName".so
    echo Ouput: "$fileName".so
elif [[ $mode = "2" ]]; then #whole folder
    echo "Please type the full folder path:"
    read folderPath

    for filePath in $folderPath/*; do
        full_fileName=$(basename -- "$filePath")
        fileName="${full_fileName%.*}"
        extension="${full_fileName##*.}"
        if [[ $fileType = "1" && $extension = "py" ]]; then
            python3 setup.py $fileName build_ext --inplace
            echo Ouput: "$fileName".so
        elif [[ $fileType = "2" && $extension = "pkl" ]]; then
            python3 encode_pkl.py $filePath $fileName
            python3 setup.py $fileName build_ext --inplace
            rm "$fileName".py
            rm "$fileName".c
            mv "$fileName".*.so "$fileName".so
            echo Ouput: "$fileName".so
        elif [[ $fileType = "3" && $extension = "h5" ]]; then #.h5
            python3 encode_h5.py $filePath $fileName
            python3 setup.py $fileName build_ext --inplace
            rm "$fileName".py
            rm "$fileName".c
            mv "$fileName".*.so "$fileName".so
            echo Ouput: "$fileName".so
        fi
    done
fi
