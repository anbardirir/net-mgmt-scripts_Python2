#!/usr/bin/python


# The goal of this script was to try and make use of eapi with out having to create host and cli_command file
# Keeping the script interactive
# Needless to say its buggy and eapi does not accept partial command syntax
# Not a real functional script
# Keeping this as a work in progress

from jsonrpclib import Server

UN = "<>"
PW = "<>"
EPW = "<>"

device_list = []
while (True):
    units = raw_input('Enter devices one at a time press enter after each. Type exit when done:\n ')
    if units == 'exit': break
    device_list.append(units)

print device_list

host_commands = [{ "cmd": "enable", "input": EPW}]

host_commands = []
while (True):
    host_command = raw_input('Enter configuration one line at a time. Hit Enter after each line. Type exit when done:\n ')
    if host_command == 'exit': break
    host_commands.append(host_command)
print host_commands

for ip in device_list:
    switch = Server ("http://%s:%s@%s/command-api" % (UN, PW, ip))
    response = switch.runCmds( 1,host_commands, 'json')
    print response


