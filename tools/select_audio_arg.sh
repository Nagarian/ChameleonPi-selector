#! /bin/bash

mydir=$(pwd)

cd /opt/selector/tools

CHOICE=$1


if [ "$CHOICE" == "" ]; then
	echo Cancel
	exit
fi

case $CHOICE in
	0) ;;
	1) ;;
	2) ;;
esac

echo \#! /bin/sh > set_audio.sh
chmod +x set_audio.sh

case $CHOICE in
	0)
	sudo sed -i 's/^hdmi_drive/#hdmi_drive/g' /boot/config.txt
	exit
	;;
	1) 
	sudo sed -i 's/^#hdmi_drive/hdmi_drive/g' /boot/config.txt
	sudo sed -i 's/hdmi_drive=2/hdmi_drive=1/g' /boot/config.txt
	echo amixer cset numid=3 $CHOICE >> set_audio.sh
	;;
	2) 
	sudo sed -i 's/^#hdmi_drive/hdmi_drive/g' /boot/config.txt
	sudo sed -i 's/hdmi_drive=1/hdmi_drive=2/g' /boot/config.txt
	echo amixer cset numid=3 $CHOICE >> set_audio.sh

	;;
esac

./set_audio.sh



cd $mydir