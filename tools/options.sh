#! /bin/bash
while :
do

	cmd=(dialog --keep-tite --menu "ChameleonPI extra menu:" 22 76 16)

	options=( 	1 "Open terminal"
			  	2 "Resize roms partition"
		      	3 "Reboot now"
				4 "Reset some emulators config"
				5 "Audio menu"
				6 "Raspbian config (overscan, locales, memory_split...)"
			)

	choices=$("${cmd[@]}" "${options[@]}" 2>&1 >/dev/tty)

	retval=$?

	case $retval in
	  1) exit ;;
	  255) exit ;;
	esac


	clear

	for choice in $choices
	do
		case $choice in
			2)
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
				sudo reboot 
				;;

			4)
				cd /opt/selector/tools/
				./emconfig_reset.sh
				echo done!
				;;			
			5)
				cd /opt/selector/tools/
				./select_audio.sh
				;;	

			6)
				sudo raspi-config
				;;

			9)
				exit
				;;

		esac
	done

done
