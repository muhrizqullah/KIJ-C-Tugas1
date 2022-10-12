#!/bin/bash

encryptionMethods=("aes" "des" "rc4" "diy_aes" "diy_des")
files=("final.txt" "quote.jpg" "teaser.mp4")
count=1
csv="run-output-demo.csv"

echo "no,fileName,encryptionMethod,encryptionTime,decryptionTime" > $csv

for i in "${encryptionMethods[@]}"; do
    for j in "${files[@]}"; do
        folder="output/$i/$j"
        mkdir -p $folder

        for k in $(seq $count); do
        
            echo "Uploading $j with $i encryption for the $k time"
            py client.py upload $i \"$j\" > "$folder/uploading-$k.txt"
            encTime=$(grep "Time taken for encryption:" "$folder/uploading-$k.txt" | cut -d " " -f 5)

            echo "Downloading $j with $i encryption for the $k time"
            py client.py download $i \"$j\" > "$folder/downloading-$k.txt"
            decTime=$(grep "Time taken for decryption:" "$folder/downloading-$k.txt" | cut -d " " -f 5)

            echo "$k,$j,$i,$encTime,$decTime" >> $csv

            # rm "files/$j"
        done
    done
done