#! /bin/bash

cmd=(dialog --keep-tite --menu "ChameleonPI audio menu:" 22 76 16)

options=(0 "Auto audio"
	 1 "3.5mm socket"
	 2 "HDMI" )

CHOICE=$("${cmd[@]}" "${options[@]}" 2>&1 >/dev/tty)

retval=$?

case $retval in
	 1) exit ;;
	 255) exit ;;
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


