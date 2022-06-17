#!/usr/bin/bash
# author: Bl4ky113

# Download images for the proyect, 
# mostly rough collie dogs and
# any kind of cat

images_urls=`cat .images_urls`
index=1

for url in $images_urls
do
    curl -o "image_$index.jpg" $url
    index=$(($index + 1))
done
