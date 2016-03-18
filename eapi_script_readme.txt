To use the eapi script you will need to create two text files that will be openned when you run the script.
The first is your device list. In that file you will simply add the ip addresses or host names of the devices your going to run your script on. That file should be saved as device_list.txt. 

10.0.0.x
10.0.0.y
10.0.0.z
-or-
test-router1
test-router2
test-router3

The second file you will need to create is the commands file. Called cli_commands.txt. The script is written like you were going to configure a device.

configure
 interface ethernet 1
 shutdown
 exit
show interfaces ethernet 1

Then to run the script all you would need to do is enter the following from command line
./eapi_script.py

