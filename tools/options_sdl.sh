#! /bin/bash

mydir=$(pwd)


while :
do
	cd $mydir

	CHOICE=$(../menusel.py options.conf)

	if [ "$CHOICE" == "" ]; then
		echo Cancel
		exit
	fi

	clear

	case $CHOICE in
		0)
			echo exit
			exit
			;;
		99)
			echo exit
			exit
			;;
		2)
			echo resizing
			cd /opt/selector/tools/
			echo Resizing...
			sudo ./cpi_resize.sh
			echo done!
			;;
		1)
			cd
			/bin/bash
			;;

		3)
			echo reboot
			sudo reboot 
			;;

		4)
			cd /opt/selector/tools/
			./emconfig_reset.sh
			echo done!
			;;			
		5)
			cd /opt/selector/tools/
			./select_audio_sdl.sh
			;;	

		6)
			sudo raspi-config
			;;

	esac

done
