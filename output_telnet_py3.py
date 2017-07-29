root@debian:/home/todd/gns3# python3 telnet_py3.py 
Enter host IPs u want to connect to seperate with space: 192.168.10.1 192.168.10.2 192.168.10.3
Enter cmd seperate with a ',' : show ip int brief , show clock
Username: cisco
Password: 

R1#term length 0
R1#show ip int brief 
Interface              IP-Address      OK? Method Status                Protocol
FastEthernet0/0        192.168.10.1    YES manual up                    up      
FastEthernet1/0        unassigned      YES unset  up                    up      
FastEthernet1/1        unassigned      YES unset  administratively down down    
Serial2/0              unassigned      YES unset  administratively down down    
Serial2/1              unassigned      YES unset  administratively down down    
Serial2/2              unassigned      YES unset  administratively down down    
Serial2/3              unassigned      YES unset  administratively down down    
R1# show clock
*23:36:05.550 UTC Fri Jul 28 2017
R1#exit


R2#term length 0
R2#show ip int brief 
Interface              IP-Address      OK? Method Status                Protocol
FastEthernet0/0        192.168.10.2    YES manual up                    up      
FastEthernet1/0        unassigned      YES unset  up                    up      
FastEthernet1/1        unassigned      YES unset  administratively down down    
Serial2/0              unassigned      YES unset  administratively down down    
Serial2/1              unassigned      YES unset  administratively down down    
Serial2/2              unassigned      YES unset  administratively down down    
Serial2/3              unassigned      YES unset  administratively down down    
R2# show clock
*23:29:28.354 UTC Fri Jul 28 2017
R2#exit


R3#term length 0
R3#show ip int brief 
Interface              IP-Address      OK? Method Status                Protocol
FastEthernet0/0        192.168.10.3    YES manual up                    up      
FastEthernet1/0        unassigned      YES unset  up                    up      
FastEthernet1/1        unassigned      YES unset  administratively down down    
Serial2/0              unassigned      YES unset  administratively down down    
Serial2/1              unassigned      YES unset  administratively down down    
Serial2/2              unassigned      YES unset  administratively down down    
Serial2/3              unassigned      YES unset  administratively down down    
R3# show clock
*23:52:08.634 UTC Fri Jul 28 2017
R3#exit

root@debian:/home/todd/gns3# 

