
#This is the telnet Library for Python3 
#Make sure transport input telnet is enabled on router validate

from getpass import getpass
import telnetlib

HOST = input("What host do you want to connect to: ")
user = input("Username: ")
password = getpass("Password: ")


tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"term length 0\n")
tn.write(b"show run \n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))

