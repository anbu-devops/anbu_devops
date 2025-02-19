import re

def parse_ipconfig(ipconfig_output):
    interfaces = {}
    current_interface = None
    
    for line in ipconfig_output.split('\n'):
        
        line = line.strip()
        #print(line)
        if "adapter" in line:
            current_interface = line.split('adapter ')[-1].strip(':')
            #print(current_interface)
            interfaces[current_interface] = {}
        
        elif current_interface:
            if 'IPv4 Address' in line:
                match = re.search(r'IPv4 Address[ .]*: ([\d\.]+)', line)
                if match:
                    interfaces[current_interface]['ipv4'] = match.group(1)
            
            elif 'Subnet Mask' in line:
                match = re.search(r'Subnet Mask[ .]*: ([\d\.]+)', line)
                if match:
                    interfaces[current_interface]['subnet_mask'] = match.group(1)
    
    return interfaces

ipconfig_output = """Ethernet adapter Ethernet 3:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : PANGP Virtual Ethernet Adapter Secure
   Physical Address. . . . . . . . . : 02-50-41-00-00-01
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   IPv6 Address. . . . . . . . . . . : fd53:5043:5000:f90c::90(Preferred)
   IPv4 Address. . . . . . . . . . . : 10.249.12.144(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.255
   Default Gateway . . . . . . . . . :
   DHCPv6 IAID . . . . . . . . . . . : 218255425
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2B-B5-59-5F-48-68-4A-32-7E-C2
   DNS Servers . . . . . . . . . . . : 10.198.80.20
                                       10.39.50.20
   NetBIOS over Tcpip. . . . . . . . : Disabled

Wireless LAN adapter Local Area Connection* 1:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Microsoft Wi-Fi Direct Virtual Adapter
   Physical Address. . . . . . . . . : 48-68-4A-32-7E-C3
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Wireless LAN adapter Local Area Connection* 2:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Microsoft Wi-Fi Direct Virtual Adapter #2
   Physical Address. . . . . . . . . : 4A-68-4A-32-7E-C2
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Wireless LAN adapter Wi-Fi:

   Connection-specific DNS Suffix  . : lan
   Description . . . . . . . . . . . : Intel(R) Wi-Fi 6 AX201 160MHz
   Physical Address. . . . . . . . . : 48-68-4A-32-7E-C2
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::4652:1109:dcf9:d3a0%23(Preferred)
   IPv4 Address. . . . . . . . . . . : 192.168.31.64(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . . : 13 February 2025 10:32:18
   Lease Expires . . . . . . . . . . : 14 February 2025 20:27:22
   Default Gateway . . . . . . . . . : 192.168.31.1
   DHCP Server . . . . . . . . . . . : 192.168.31.1
   DHCPv6 IAID . . . . . . . . . . . : 306735178
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2B-B5-59-5F-48-68-4A-32-7E-C2
   DNS Servers . . . . . . . . . . . : 192.168.31.1
   NetBIOS over Tcpip. . . . . . . . : Disabled

Ethernet adapter vEthernet (Default Switch):

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Hyper-V Virtual Ethernet Adapter
   Physical Address. . . . . . . . . : 00-15-5D-16-6C-00
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::dc56:e1e7:8e4f:cad6%26(Preferred)
   IPv4 Address. . . . . . . . . . . : 172.18.224.1(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Default Gateway . . . . . . . . . :
   DHCPv6 IAID . . . . . . . . . . . : 436213085
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2B-B5-59-5F-48-68-4A-32-7E-C2
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter vEthernet (WSL (Hyper-V firewall)):

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Hyper-V Virtual Ethernet Adapter #2
   Physical Address. . . . . . . . . : 00-15-5D-CE-2D-94
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::238a:722e:ec98:c359%63(Preferred)
   IPv4 Address. . . . . . . . . . . : 172.17.32.1(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Default Gateway . . . . . . . . . :
   DHCPv6 IAID . . . . . . . . . . . : 1056970077
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2B-B5-59-5F-48-68-4A-32-7E-C2
   NetBIOS over Tcpip. . . . . . . . : Enabled

 """
parsed_data = parse_ipconfig(ipconfig_output)
print(parsed_data)
