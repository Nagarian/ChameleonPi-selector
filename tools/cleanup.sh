#!/bin/bash

./umountall.sh
./emconfig_set.sh


rm -r /roms/amiga/*
rm -r /roms/amstrad/disk/*
rm -r /roms/amstrad/tape/*
rm -r /roms/samcoupe/*
rm -r /roms/appleii/*
rm -r /roms/atari800/*
rm -r /roms/atarist/*
rm -r /roms/atarivcs/*
rm -r /roms/c64/*
rm -r /roms/dos/*
rm -r /roms/gameboy/*
rm -r /roms/mame/rom/*
rm -r /roms/megadrive/*
rm -r /roms/msx/*
rm -r /roms/nes/*
rm -r /roms/oric/*
rm -r /roms/samcoupe/*
rm -r /roms/scummvm/*
rm -r /roms/snes/*
rm -r /roms/spectrum/*
rm -r /roms/snes/*
rm -r /roms/vic20/*
rm -r /roms/vmac/*
rm -r /roms/zx81/*

rm /roms/*.squashfs
rm -r /roms/.squash/*

rm -r /roms/USB/*


cd /
sudo find -name *DS_Store* -exec rm -r {} \;
sudo find -name ._.Trashes -exec rm -r {} \;
sudo find -name .Spotlight-V100 -exec rm -r {} \;
sudo find -name .fseventsd -exec rm -r {} \;
sudo find -name .Trashes -exec rm -r {} \;
sudo find ./ -name '*~' -exec rm '{}' \; -print -or -name ".*~" -exec rm {} \; -print


cd /roms/
sudo find -name *DS_Store* -exec rm -r {} \;
sudo find -name ._.Trashes -exec rm -r {} \;
sudo find -name .Spotlight-V100 -exec rm -r {} \;
sudo find -name .fseventsd -exec rm -r {} \;
sudo find -name .Trashes -exec rm -r {} \;
sudo find ./ -name '*~' -exec rm '{}' \; -print -or -name ".*~" -exec rm {} \; -print


sudo apt-get clean


