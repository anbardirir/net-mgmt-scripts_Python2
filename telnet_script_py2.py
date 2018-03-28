from __future__ import print_function
import getpass
import telnetlib
user = raw_input("Enter your username: ")
password = getpass.getpass()

host = raw_input("Enter hostnames or IPs seperated by space : ")
cmd = raw_input("Enter commands serperated with ',': ")

#Create lists to iterate through
hosts = host.split()
cmds = cmd.split(",")

for HOST in hosts:
    print("Connecting to host:",  HOST)
    tn = telnetlib.Telnet(HOST)
    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
	tn.write(password + "\n")
        tn.write("enable\n")
        tn.write(password +"\n")
	tn.write("terminal length 0\n")
        for CMD in cmds:
            tn.write(CMD + "\n")
	tn.write("exit\n")

    readoutput = tn.read_all()
    saveoutput =  open("router_" + HOST, "w")
    saveoutput.write(readoutput)
    saveoutput.write("\n")
    saveoutput.close
print(readoutput)
