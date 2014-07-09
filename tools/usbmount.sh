#! /bin/bash

#not sudo stop

./umountusb.sh

#mount
let DRIVE=0

mkdir /roms/USB > /dev/null 2>&1 &

function mountdrive 
{
	if [ -b $1 ]
	then
		let DRIVE=$DRIVE+1
		mkdir /roms/USB/Vol$DRIVE
		sudo mount $1 /roms/USB/Vol$DRIVE
	fi
} 


FILES=/dev/sd??

for f in $FILES
do
	echo "Mount $f file..."
	
	mountdrive $f

done


