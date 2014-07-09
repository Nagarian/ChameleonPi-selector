#! /bin/sh


SERVER=$(smbtree -N -b | grep CHAMELEONROMS | cut -d"\\" -f3)
SHARE=$( smbtree -N -b | grep CHAMELEONROMS | cut -d"\\" -f4)

#echo $SERVER
SERVERIP=$( nmblookup -R  -N $SERVER | grep $SERVER'<00>' | cut -d' ' -f1 )

#echo $SERVERIP $SHARE

sudo mount //$SERVERIP/$SHARE /roms -o guest,rw,noexec,uid=1001,gid=1001

cd /opt/selector/tools
