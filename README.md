![ChameleonPi](http://chameleon.enging.com/data1/images/cpi_h6.jpg)

This repo is a fork of ChameleonPi selector Menu.


Visit [ChameleonPi Website](http://chameleon.enging.com/) to learn more.

## Installing

To install this version of selector you must :

1. Install ChameleonPi OS on your SD card
2. Download and execute installUpdate.sh of this repo, it will backup your current /opt/selector folder and download it directly from here ! You can execute this command to download it :

> wget https://raw.githubusercontent.com/Nagarian47/ChameleonPi-selector/master/installUpdate.sh
> chmod u+x installUpdate.sh 
> ./installUpdate.sh

3. Custom your own configuration (take a look at /opt/selector/configuration files
4. Enjoy !

## Custom selector

I've made some improvement to the initial project, and begin with pass it to oriented object version, so now it will be easier to custom the entire layout of the selector.

I'm inspiriting from Microsoft XNA project to structure the all the project, so you can find every frame (emulator choice, game choice and options) on the related folder.
They all follow the same structure, which is describe in the frame/IFrame.py file

###Among the new features, you can find :
* The selector was more fluid and faster than before
* The possibility to easily change the resolution. By default your are on 1920*1080, but we have made compatible with 1280*1024 (4:3 resolution). NB: you must also update /boot/config.txt file to optimize the resolution; NB2: in 1280*1024 the navigator wasn't available, so you can't have some help :(
* You can access to more options, in the relative menu (I've map most options from tools folder but i didn't test them all)
* You have more sound on the menu
* I've fork two other project, Retrogame, and PiArcade. The first enable keys from GPIO pins of the Raspberry Pi, and the second add the ability to use the pins provided by an MCP23017 I2C port expander to play with a friend. I recommend to you to take a look at the main branch, it must be up-to date. But for piarcade, I wan to precise that the original script doesn't work for me. So I've customize it to work, but it's not really optimized. To know how to use MCP23017, you can [read this](http://www.raspberrypi-spy.co.uk/2013/07/how-to-use-a-mcp23017-i2c-port-expander-with-the-raspberry-pi-part-1/)
* Now you can choose every console game by the selector interface
* Game selector can display only desired file NB: it's based on the extensions name, and it's configured on configuration/machines.conf file

###But I've made some regression
* For needed of my project, I've clean console list, and only let 7 consoles. I don't re-add others because I've modified machines.conf structures. But you can made it, you have only two file to modify : configuration/manchines.conf and select.sh
* By default, on the game selector menu, you're chroot to the roms folder consoles. By this way, you can use your raspberry pi with less risks everywhere

