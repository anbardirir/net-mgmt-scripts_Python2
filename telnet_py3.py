
#This is the telnet Library for Python3
#Make sure transport input telnet is enabled on router validate

from getpass import getpass
import telnetlib

host = input("Enter host IPs u want to connect to seperate using a space : ")
cmd = input("Enter cmd seperate with a ',' : ")
user = input("Username: ")
password = getpass("Password: ")

#create lists to iterate through
hosts = host.split()
cmds = cmd.split(",")

for HOST in hosts:
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"term length 0\n")
    #iterate through cmds using for loop
    for CMD in cmds:
        tn.write(CMD.encode('ascii') + b"\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))

