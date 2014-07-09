#! /bin/bash

#umount

sudo umount /roms/USB/*  > /dev/null 2>&1 
sudo umount -f /roms/USB/*  > /dev/null 2>&1 &
sudo umount -l /roms/USB/* > /dev/null 2>&1 &

rm -r /roms/USB > /dev/null 2>&1 &

