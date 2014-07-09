#!/bin/bash

TITOL=$1
CARPETA=$2
EXECUTABLE=$3

while :
do

	FILE=$(dialog --stdout --title "$TITOL - Press space to select the file, enter to run" --fselect $CARPETA 15 80 )

	echo $FILE

	if [ -e "$FILE" ] 
	then
		$EXECUTABLE "$FILE"

	else
		exit
	fi

done
