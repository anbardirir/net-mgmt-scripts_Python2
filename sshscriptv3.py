__author__ = "twr14152"
#
#
import paramiko
import time
import getpass

UN = raw_input("Username : ")
PW = getpass.getpass("Password : ")

#Create two text files "device_list.txt" and "cli_commands.txt"
device_list = []
file1 = open('device_list.txt', 'r')
for line in file1:
    device_list.append(line.strip())
file1.close()
print device_list

host_commands = []
file2 = open('cli_commands.txt', 'r')
for line in file2:
    host_commands.append(line.strip())
file2.close()
print host_commands

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
        time.sleep(1)
        buf = remote.recv(65000)
        print buf
        file3 = open('sshlogfile0001.txt', 'a')
        file3.write(buf)
        file3.close()
    twrssh.close()

