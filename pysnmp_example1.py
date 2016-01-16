from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

# Run through these hosts
IP = ['10.10.10.110', '10.10.10.120', '10.10.10.130']
#
#http://tools.cisco.com/Support/SNMP/do/BrowseOID.do?local=en&translate=Translate&objectInput=1.3.6.1.2.1.1.1#oidContent
#
def main():
    for ip in IP:
        errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
            cmdgen.CommunityData('password'),
            cmdgen.UdpTransportTarget((ip, 161)),
            cmdgen.MibVariable('SNMPv2-MIB', 'sysName', 0),
            cmdgen.MibVariable('SNMPv2-MIB', 'sysDescr', 0),
            lookupNames=True, lookupValues=True
)

        # Check for errors and print out results
        if errorIndication:
            print(errorIndication)
        elif errorStatus:
            print(errorStatus)
        else:
            for name, val in varBinds:
                print('%s = %s\n' % (name.prettyPrint(), val.prettyPrint()))

if __name__ == '__main__':
   main()

~       