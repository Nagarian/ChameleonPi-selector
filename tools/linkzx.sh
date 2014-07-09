#!/bin/bash

cd /roms

FILES=*
for f in $FILES
do
	echo "Processing $f file..."
	rm /home/zx/$f
	ln -s /roms/$f /home/zx/$f
done

cd /opt/selector/tools

