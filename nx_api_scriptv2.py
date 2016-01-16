# This was my attempt to use the sandbox that comes with the Nexus9K to make an interactive script.
# As posted in the sandbox the output would not print in a readable fashion. Had to remove .json() at the end of the post command.
# Then add the print response.text. Then it started posting a readable output
#
import requests
import json
import getpass

UN = raw_input("Username: ")
PW = getpass.getpass("Password: ")
IP = raw_input("Host address or name: ")
command = raw_input("Commands: ")

url='http://%s/ins' % IP
switchuser=UN
switchpassword=PW

myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": command,
      "version": 1
    },
    "id": 1
  }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword))
print response.text
