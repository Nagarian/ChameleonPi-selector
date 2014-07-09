#!/bin/bash

sudo sync

mount | grep cifs | grep /roms | cut -d' ' -f3 | awk '{ system("sudo umount " $1 ); }'



