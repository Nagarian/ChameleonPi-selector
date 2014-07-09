#!/bin/bash

sudo sync

mount | grep unionfs-fuse | grep /roms/ | cut -d' ' -f3 | awk '{ system("sudo umount " $1 ); }'

sudo umount /roms/.squash/*.squashfs



