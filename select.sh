#! /bin/bash

choice=3

_main ()
{


	cd /opt/selector
	# clear
	
	fileSelected=$(python selector.py $choice)
	choice=$?

	#if (([ $choice -ge 2 ] && [ $choice -le 8 ]) || [ $choice -lt 53 ] ) && [ ! -e "$fileSelected" ]
	#then
	#	_main
	#fi

	case $choice in
		2)
			stella "$fileSelected"
			_main ;;
		3) 
			retroarch -L /usr/lib/libretro-imame4all.so "$fileSelected"
			_main ;;
		4)
			/opt/dgen-sdl-1.32/dgen "$fileSelected"
			_main ;;
		5)
			retroarch -L /opt/ra_cores/pocketsnes-libretro/libretro.so "$fileSelected"
			_main ;;
		6)
			retroarch -L /usr/lib/libretro-fceu.so "$fileSelected"
			_main ;;
		7)
			/opt/gnuboy-1.0.3.orig/sdlgnuboy --scale=4 "$fileSelected"
			_main ;;
		8)
			VisualBoyAdvance --auto-frameskip "$fileSelected"
			_main ;;
		53)
			advmenu "$fileSelected"
			_main ;;


		101)
		cd
		/bin/bash
		exit ;;

		102)
			sudo halt
			exit;;

		103)
			sudo reboot
			exit;;

		141)
			/opt/selector/tools/usbmount.sh
			_main ;;
		142)
			/opt/selector/tools/umountusb.sh
			_main ;;
		143)
			/opt/selector/tools/netroms.sh
			_main ;;
		144)
			/opt/selector/tools/umountnetroms.sh
			_main ;;
		145)
			/opt/selector/tools/mountsquasfs.sh
			_main ;;
		146)
			/opt/selector/tools/umountsquasfs.sh
			_main ;;
		147)
			/opt/selector/tools/umountall.sh
			_main ;;

		151)
			/opt/selector/tools/select_audio_arg.sh 0
			_main ;;
		152)
			/opt/selector/tools/select_audio_arg.sh 1
			_main ;;
		153)
			/opt/selector/tools/select_audio_arg.sh 2
			_main ;;

		161)
			/opt/selector/tools/emconfig_reset.sh
			_main ;;
		162)
			/opt/selector/tools/cpi_resize.sh
			_main ;;
		163)
			sudo raspi-config
			_main ;;
		164)
			/opt/selector/tools/cleanup.sh
			_main ;;


		199)
		cd /opt/selector/tools
		./options_sdl.sh
		exit ;;

		0)
			sudo halt
			exit ;;
		1)
			# clear
			exit ;;
	esac
}

if [[ $(who am i) =~ \([0-9\.]+\)$ ]]; then echo ; else _main; fi
#_main


