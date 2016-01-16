#
import paramiko
import time
import getpass
import os
from host_file import device_list
from commands_file import host_commands

UN = raw_input("Username : ")
PW = getpass.getpass("Password : ")

# For loop allows you to specify number of hosts
for ip in device_list:
    print ip
    twrssh = paramiko.SSHClient()
    twrssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    twrssh.connect(ip, port=22, username=UN, password=PW)
    remote = twrssh.invoke_shell()
    remote.send('term len 0\n')
    remote.send('enable\n')
    remote.send('%s\n' % PW)
    time.sleep(1)
    #This for loop allows you to specify number of commands  you want to enter
    #Dependent on the output of the commands you may want to tweak sleep time.
    for commands in host_commands:
        remote.send(' %s \n' % commands)
        time.sleep(2)
        buf = remote.recv(65000)
        print buf
        f = open('sshlogfile0001.txt', 'a')
        f.write(buf)
        f.close()
    twrssh.close()

