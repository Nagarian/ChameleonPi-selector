#!/bin/bash

./umountsquashfs.sh

FILES=/roms/*.squashfs

for f in $FILES
do
	echo "Mount $f file..."
	
	filename=$(basename "$f")
	extension="${filename##*.}"
	filename2="${filename%.*}"

	#if [ "$filename2" -ne "" ]
	#then

		mkdir -p "/roms/.squash/$filename"
		mkdir -p "/roms/.squash/$filename2"_rw
		mkdir -p "/roms/$filename2"
	
		sudo mount -t squashfs $f /roms/.squash/$filename -o ro,loop

		sudo unionfs-fuse -o allow_other,cow,nonempty "/roms/.squash/$filename"=RO:"/roms/.squash/$filename2"_rw=RW  "/roms/$filename2"

	#fi

done



