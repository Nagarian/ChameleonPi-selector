#!/bin/bash

#removing possible previous temp file
rm list.temp 2>/dev/null

#scans for wifi connections & isolates wifi AP name
# thanks to jonjgc for the array solution
#thanks to ghostdog74 for the AWK suggestion

eval list=( $(sudo iwlist scan 2>/dev/null | awk -F":" '/ESSID/{print $2}') )

#sets prompt
PS3="Choose wifi connection: "

#tests for number of wifi connections, exits if none
if [ -z "${list[0]}" ]; then
	clear
	echo "No available wifi connection"
	exit 1
fi

#menu of wifi connections
select item in "${list[@]}"; do

#sets essid as value for WIFI variable and displays information about the AP
	wifi=$(echo $item)
        sudo iwlist scan 2>/dev/null | sed -n "/$wifi/, +9p" > list.temp
	echo "$(cat list.temp | sed 's/^[ \t]*//')"

#sets channel as value for CHANNEL variable
	channel=$(grep Channel: list.temp | sed 's/.*Channel://g')

#test for mode, if mode = master, sets MODE variable to managed
	mode=$(grep Mode list.temp | sed 's/.*Mode://g')
	if [ "$mode" == "Master" ]; then
		mode="managed"
	else
		clear
		echo "Cannot connect"
		exit
	fi

#tests for encryption key
	key=$(grep key: list.temp | sed 's/.*key://g')
	if [ "$key" == "on" ]; then
		echo -n "Enter encryption key: "
		read key
	fi

#checks encryption algorithm
	IE=$(grep IE list.temp | sed 's/^ .*IE: \(...\).*/\1/')

#writes to /etc/network/interfaces file for WPA encryption: essid, key, protocols, etc.
	if [ "$IE" == "WPA" ]; then
		sudo cp /etc/network/interfaces /etc/network/interfaces.bakup
		sudo sed -i 's/iface wlan0 inet manual/iface wlan0 inet dhcp/' /etc/network/interfaces
		sudo sed -i -e "/dhcp/a\wpa-passphrase $key" \
	-e "/dhcp/a\wpa-driver wext" \
	-e "/dhcp/a\wpa-key-mgmt WPA-PSK" \
	-e "/dhcp/a\wpa-proto WPA" \
	-e "/dhcp/a\wpa-ssid \"$wifi\"" /etc/network/interfaces
	sudo /etc/init.d/networking restart
	sudo cp /etc/network/interfaces.bakup /etc/network/interfaces
	sudo rm /etc/network/interfaces.bakup
	exit

	else

#sets the wireless configuration for non WPA: essid, channel, mode, key, etc
		sudo iwconfig wlan0 essid \""$wifi"\" channel $channel mode $mode key $key
		echo "------------------------------------------------"
		echo "Connecting to: $wifi at channel: $channel, mode: $mode"
		echo "------------------------------------------------"

#connects to wifi connection
		sudo dhclient
		exit
	fi
done
