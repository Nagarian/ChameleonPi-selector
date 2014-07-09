mv /opt/selector /opt/selector.bak
git clone --recursive https://github.com/Nagarian47/ChameleonPi-selector.git /opt/selector

chmod 644 /opt/selector/wifiwpa.config
chmod 644 /opt/selector/singleton.py
chmod 755 /opt/selector/select.sh
chmod 755 /opt/selector/selector.py
chmod 644 /opt/selector/frameCollection.py
chmod 644 /opt/selector/chame.sublime-workspace
chmod 644 /opt/selector/chame.sublime-project

chmod 755 /opt/selector/tools/wifi.sh
chmod 755 /opt/selector/tools/usbmount.sh
chmod 755 /opt/selector/tools/umountusb.sh
chmod 755 /opt/selector/tools/umountsquashfs.sh
chmod 755 /opt/selector/tools/umountnetroms.sh
chmod 755 /opt/selector/tools/umountall.sh
chmod 755 /opt/selector/tools/testjoy.py
chmod 644 /opt/selector/tools/set_audio.sh.cpi
chmod 755 /opt/selector/tools/set_audio.sh
chmod 755 /opt/selector/tools/select_audio.sh
chmod 755 /opt/selector/tools/select_audio_arg.sh
chmod 755 /opt/selector/tools/runmegadrive.sh
chmod 755 /opt/selector/tools/retrogame
chmod 755 /opt/selector/tools/piarcade
chmod 755 /opt/selector/tools/options.sh
chmod 755 /opt/selector/tools/options_sdl.sh
chmod 755 /opt/selector/tools/netroms.sh
chmod 755 /opt/selector/tools/mountsquashfs.sh
chmod 755 /opt/selector/tools/listroms.sh
chmod 755 /opt/selector/tools/linkzx.sh
chmod 755 /opt/selector/tools/emconfig_set.sh
chmod 755 /opt/selector/tools/emconfig_reset.sh
chmod 644 /opt/selector/tools/daemon
chmod 755 /opt/selector/tools/cpi_resize.sh
chmod 755 /opt/selector/tools/cpi_resize_old.sh
chmod 755 /opt/selector/tools/cleanup.sh
chmod 755 /opt/selector/tools/AUTOEXEC.system
chmod 755 /opt/selector/tools/AUTOEXEC.launcher

chmod 644 /opt/selector/resources/splash.psd
chmod 644 /opt/selector/resources/splash.png
chmod 644 /opt/selector/resources/splash2.png
chmod 644 /opt/selector/resources/splash2.1920x1080.png
chmod 644 /opt/selector/resources/splash.1920x1080.png
chmod 644 /opt/selector/resources/splash.1280x1024.png
chmod 644 /opt/selector/resources/sound
chmod 644 /opt/selector/resources/gamebackground.1920x1080.psd
chmod 644 /opt/selector/resources/gamebackground.1920x1080.png
chmod 644 /opt/selector/resources/gamebackground.1280x1024.psd
chmod 644 /opt/selector/resources/gamebackground.1280x1024.png
chmod 644 /opt/selector/resources/font
chmod 644 /opt/selector/resources/fonstram.psd
chmod 644 /opt/selector/resources/fonstram.png
chmod 644 /opt/selector/resources/fonstram.1920x1080.png
chmod 644 /opt/selector/resources/fonstram.1280x1024.png
chmod 644 /opt/selector/resources/fons.png
chmod 644 /opt/selector/resources/folder.png
chmod 644 /opt/selector/resources/error
chmod 644 /opt/selector/resources/consoles
chmod 644 /opt/selector/resources/error/*
chmod 644 /opt/selector/resources/consoles/*

chmod 644 /opt/selector/frame/screensaver.py
chmod 644 /opt/selector/frame/options.py
chmod 644 /opt/selector/frame/__init__.py
chmod 644 /opt/selector/frame/IFrame.py
chmod 644 /opt/selector/frame/gamechoice.py
chmod 644 /opt/selector/frame/folderExplorer.py
chmod 644 /opt/selector/frame/emchoice.py

chmod 644 /opt/selector/configuration/selectorConfig.py
chmod 644 /opt/selector/configuration/options.conf
chmod 644 /opt/selector/configuration/machines.conf.original
chmod 644 /opt/selector/configuration/machines.conf
chmod 644 /opt/selector/configuration/__init__.py

sudo rm /etc/splash.png /etc/splash2.png
sudo ln -s /opt/selector/resources/splash.png /etc/splash.png
sudo ln -s /opt/selector/resources/splash2.png /etc/splash2.png