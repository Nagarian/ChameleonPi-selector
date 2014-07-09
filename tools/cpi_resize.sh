#! /bin/bash
# first, check if a resize is really needed
DEVICE_SIZE=`parted /dev/mmcblk0 u b p | grep ^Disk | awk '{print $3}' | sed s/B//`
END_OF_FAT32_PART=`parted /dev/mmcblk0 u b p | grep "^ 3" | awk '{print $3}' | sed s/B//`

let UNALLOCATED_SIZE=$DEVICE_SIZE-$END_OF_FAT32_PART

if [ $UNALLOCATED_SIZE -lt 20000000 ]
then
  echo "Resizing of FAT partition not needed, unallocated size of SD card is $UNALLOCATED_SIZE bytes."
  exit 0
fi

umount /roms > /dev/null 2>/dev/null
umount /dev/mmcblk0p3 > /dev/null 2>/dev/null
fsck -aw /dev/mmcblk0p3 > /dev/null 2>/dev/null
# sudo parted /dev/mmcblk0 unit chs resize 3 ` parted /dev/mmcblk0 unit chs print | grep fat32 | awk '{ print $2; }' ` ` parted /dev/mmcblk0 unit chs print | grep "Disk /dev/mmcblk0:" | cut -d' ' -f3 | cut -d',' -f1 `,0,0

START_SECTOR=`parted /dev/mmcblk0 unit s print | grep "^ 3" | awk '{print $2}' | sed s/s//`
echo "Starting sector: $START_SECTOR"
fdisk /dev/mmcblk0 > /dev/null 2>/dev/null << EOF
d
3
n
p
3
$START_SECTOR

t
3
b
w
q
EOF

NEW_SIZE=`parted /dev/mmcblk0 unit mb print | grep "^ 3" | awk '{print $4}' | sed s/MB//`
# don't ask me why, but giving the exact partition size produces an error in fatresize:
#  Error: The location 7951MB is outside of the device /dev/mmcblk0.
# So we substract some MB from the given partition size in order to make the process work
let NEW_SIZE=$NEW_SIZE-220
echo "New size of FAT partition /dev/mmcblk0p3: $NEW_SIZE MB"

# workaround for fatresize: link "complete device" mmcblk0 to "upper device" mmcblk0p since the tool fatresize expects the whole device with this name
ln -s /dev/mmcblk0 /dev/mmcblk0p
fatresize -p -s ${NEW_SIZE}Mi /dev/mmcblk0p3 > /dev/null 2>/dev/null
rm /dev/mmcblk0p
mount /roms

