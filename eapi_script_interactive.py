#!/usr/bin/python
#(c) 2016 Todd Riemenschneider
# This script is interactive
# Enter the devices you want to log into
# Press Enter after each device
# Type exit to move on to entering commands
# Enter commands one line at a time
# Press Enter at the end of each line
# Type exit to send commands

from jsonrpclib import Server
from pprint import pprint
#import getpass

#UN = raw_input("Username : ")
UN = "<>"
#PW = getpass.getpass("Password : ")
PW = "<>"
#EPW = getpass.getpass("enable password: ")
EPW = "<>"


device_list = []
while (True):
    units = raw_input('Enter devices one at a time. Hit enter after each device. Type @@@@ when done.:\n ')
    if units == '@@@@': break
    device_list.append(units)

print device_list

host_commands = [{ "cmd": "enable", "input": EPW}]

while (True):
    host_command = raw_input('Enter commands one line at a time. Hit enter after each command line. Type @@@@ when done.:\n ')
    if host_command == '@@@@': break
    host_commands.append(host_command)

print host_commands

for ip in device_list:
    switch = Server ("https://%s:%s@%s/command-api" % (UN, PW, ip))
    response = switch.runCmds( 1,host_commands, 'json')
    pprint(response)



