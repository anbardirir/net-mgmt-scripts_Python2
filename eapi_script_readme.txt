
There are two EAPI scripts
++++++++
Script 1
++++++++

****************
./eapi_script.py
****************
This script was used to configure devices using eapi. To use the eapi script you will need to create two text files that will be openned when you run the script. The first test file will be your device list. In that file you will simply add the ip addresses or host names of the devices your going to run your script on. That file should be saved as device_list.txt. 

10.0.0.x
10.0.0.y
10.0.0.z
-or-
test-router1
test-router2
test-router3

The second file you will need to create is the commands file. Called cli_commands.txt. The script is written like you were going to configure a device. It should be noted that commands need to be fully typed out, eapi does not accept short hand (e.g show int).


Example of config file and host file.

 ~/python_scripts/eapi_scripts $ cat cli_commands.txt
configure
interface loopback 100
description test

show interfaces loopback100
show version
exit
exit

~/python_scripts/eapi_scripts $ cat device_list.txt
sw1

sw2



Then to run the script all you would need to do is enter the following from command line

chmod 755 eapi_script.py

./eapi_script.py

~/python_scripts/eapi_scripts $ ./eapi_script_lab.py
['sw1', 'sw2']
[{'input': '<>', 'cmd': 'enable'}, 'configure', 'interface loopback 100', 'description test', 'show interfaces loopback100', 'show version', 'exit', 'exit']
[{},
 {},
 {},
 {},
 {u'interfaces': {u'Loopback100': {u'bandwidth': 0,
                                   u'description': u'test',
                                   u'forwardingModel': u'routed',
                                   u'hardware': u'loopback',
                                   u'interfaceAddress': [],
                                   u'interfaceStatus': u'connected',
                                   u'lastStatusChangeTimestamp': 1465570004.7202916,
                                   u'lineProtocolStatus': u'up',
                                   u'mtu': 65535,
                                   u'name': u'Loopback100'}}},
 {u'architecture': u'i386',
  u'bootupTimestamp': 1453212810.73,
  u'hardwareRevision': u'02.01',
  u'internalBuildId': u'a9a9feba-9657-4bfd-b7a0-7875a5f7ed5e',
  u'internalVersion': u'4.15.3F-2812776.4153F',
  u'memFree': 816832,
  u'memTotal': 3978152,
  u'modelName': u'DCS-7150S-24-F',
  u'serialNumber': u'JPE14242141',
  u'systemMacAddress': u'00:1c:73:69:62:17',
  u'version': u'4.15.3F'},
 {},
 {}]
[{u'messages': [u'Warning: Password input may be echoed.\nPassword: \n']},
 {},
 {},
 {},
 {u'interfaces': {u'Loopback100': {u'bandwidth': 0,
                                   u'description': u'test',
                                   u'forwardingModel': u'routed',
                                   u'hardware': u'loopback',
                                   u'interfaceAddress': [],
                                   u'interfaceStatus': u'connected',
                                   u'lastStatusChangeTimestamp': 1465570547.2242851,
                                   u'lineProtocolStatus': u'up',
                                   u'mtu': 65535,
                                   u'name': u'Loopback100'}}},
 {u'architecture': u'i386',
  u'bootupTimestamp': 1453215305.75,
  u'hardwareRevision': u'02.01',
  u'internalBuildId': u'a9a9feba-9657-4bfd-b7a0-7875a5f7ed5e',
  u'internalVersion': u'4.15.3F-2812776.4153F',
  u'memFree': 834260,
  u'memTotal': 3978152,
  u'modelName': u'DCS-7150S-24-F',
  u'serialNumber': u'JPE14270938',
  u'systemMacAddress': u'00:1c:73:69:7e:87',
  u'version': u'4.15.3F'},
 {},
 {}]
~/python_scripts/eapi_scripts $

++++++++
Script 2
++++++++

**************************
eapi_script_interactive.py 
**************************

This script was created to use EAPI to talk with the devices but you do not need to create seperate host and command file to use.
Its more interactive.

06/18/2016 - updated script so that '@@@@' is now the break sequence rather than 'exit' for the script.
Example below reflects the output of the previous way the script was written. There were too many legitimate reasons to use the 'exit' command when configuring a device to leave it in place.

~/python_scripts/eapi_scripts $ ./eapi_script_beta.py
Enter devices one at a time. Hit enter after each device. Type exit when done.:
 sw1
Enter devices one at a time. Hit enter after each device. Type exit when done.:
 sw2
Enter devices one at a time. Hit enter after each device. Type exit when done.:
 exit
['sw1', 'sw2']
Enter commands one line at a time. Hit enter after each command line. Type exit when done.:
 configure
Enter commands one line at a time. Hit enter after each command line. Type exit when done.:
 interface loopback 100
Enter commands one line at a time. Hit enter after each command line. Type exit when done.:
 description this is a final test of eapi script
Enter commands one line at a time. Hit enter after each command line. Type exit when done.:
 show interfaces loopback 100
Enter commands one line at a time. Hit enter after each command line. Type exit when done.:
 exit
[{'input': '<>', 'cmd': 'enable'}, 'configure', 'interface loopback 100', 'description this is a final test of eapi script', 'show interfaces loopback 100']
[{},
 {},
 {},
 {},
 {u'interfaces': {u'Loopback100': {u'bandwidth': 0,
                                   u'description': u'this is a final test of eapi script',
                                   u'forwardingModel': u'routed',
                                   u'hardware': u'loopback',
                                   u'interfaceAddress': [],
                                   u'interfaceStatus': u'connected',
                                   u'lastStatusChangeTimestamp': 1465570004.7202919,
                                   u'lineProtocolStatus': u'up',
                                   u'mtu': 65535,
                                   u'name': u'Loopback100'}}}]
[{u'messages': [u'Warning: Password input may be echoed.\nPassword: \n']},
 {},
 {},
 {},
 {u'interfaces': {u'Loopback100': {u'bandwidth': 0,
                                   u'description': u'this is a final test of eapi script',
                                   u'forwardingModel': u'routed',
                                   u'hardware': u'loopback',
                                   u'interfaceAddress': [],
                                   u'interfaceStatus': u'connected',
                                   u'lastStatusChangeTimestamp': 1465570547.2242851,
                                   u'lineProtocolStatus': u'up',
                                   u'mtu': 65535,
                                   u'name': u'Loopback100'}}}]
/python_scripts/eapi_scripts $




