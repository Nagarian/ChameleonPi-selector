#! /bin/bash

umount /roms
umount /dev/mmcblk0p3
fsck -aw /dev/mmcblk0p3 
sudo parted /dev/mmcblk0 unit chs resize 3 ` parted /dev/mmcblk0 unit chs print | grep fat32 | awk '{ print $2; }' ` ` parted /dev/mmcblk0 unit chs print | grep "Disk /dev/mmcblk0:" | cut -d' ' -f3 | cut -d',' -f1 `,0,0
mount /roms


