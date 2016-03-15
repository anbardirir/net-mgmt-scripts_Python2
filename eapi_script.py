#!/usr/bin/python

from jsonrpclib import Server
import getpass
#
# I added these authentication commands so I wouldnt have to store passwords in the file.
# I also think it makes one more deliberate in their application as well as may provide some safe guards
# from inadvertantly kicking the script off
# I think it would be useful in producation. In lab testing is kind sucks.
# An option would be to simply do the following
# To work around entering passwords all the time
# comment out the current variables UN, PW, EPW, add them as static variable assignments
# UN = "password"
# PW = "password2"
# EPW = "password3"
#
UN = raw_input("Username : ")
PW = getpass.getpass("Password : ")
EPW = getpass.getpass("enable password: ")


device_list = []
#You will need to create a file device_list.txt that will have the host you want to access
file1 = open('device_list.txt', 'r')
for line in file1:
    device_list.append(line.strip())
file1.close()
print device_list

host_commands = [{ "cmd": "enable", "input": EPW}]

#You will need to create a file cli_commands.txt that will have the commands you want to run
file2 = open('cli_commands.txt', 'r')
for line in file2:
    ln = line.strip()
    if ln:
        host_commands.append(ln)
file2.close()
print host_commands

for ip in device_list:
    switch = Server ("http://%s:%s@%s/command-api" % (UN, PW, ip))
    response = switch.runCmds( 1,host_commands, 'json')
    print response

