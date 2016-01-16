### Target hosts for this script lives in nexus_host.py
import time
from nexus_hosts import network_devices
import requests
import json
import getpass


UN = raw_input("Username : ")
PW = getpass.getpass("Password : ")


#For loop allows you to specify number of hosts
for IP in  network_devices:
    print IP
    url='http://%s/ins' % IP
    switchuser=UN
    switchpassword=PW
    myheaders={'content-type':'application/json-rpc'}
    payload=[{"jsonrpc": "2.0","method": "cli", "params": {"cmd": "config t", "version": 1}, "id": 1},
             {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "interface loopback 12","version": 1},"id": 2},
             {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "description nxapi script test","version": 1},"id": 3},
             {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "end", "version": 1}, "id": 4}]
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword))
    print response.text
    ### This log file output is identical to what you see on the screen when running the script
    f = open('nxapi-logfile0001.txt', 'a')
    f.write(response.text)
    f.close()
