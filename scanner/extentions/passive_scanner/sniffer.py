#! /usr/bin/env python

import subprocess
import sys
import re
import netifaces
import socket
import time
from time import gmtime, strftime
from IPy import IP
from database import WriteToSqlite
from networking.ethernet import Ethernet
from networking.ipv4 import IPv4
from networking.pcap import Pcap



def main():
    ethinterface()
    passive_scan()

def ethinterface():
    """
    Uses the python library netifaces to enumerate a list of the interfaces
    on the system.
    Presents a list of interfaces and prompt the use to select one.
    """
    iflist = netifaces.interfaces()
    print('Interfaces found')

    for index in range(len(iflist)):
        print (index, ':', iflist[index])

    interface = input('enter interface # ')
    interface = int(interface)
    interface = iflist[interface]
#    interface = input('Enter an interface name if needed: ')
    print('interface selected is:', interface)
    print()
    return interface

def passive_scan():
   
    pcap = Pcap('capture.pcap')
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    
    exception_ip = ['0.0.0.0', '127.0.0.1', ]
    exception_ttl = ['1']

    while True:
        try:
            raw_data , addr= conn.recvfrom(65535)
            pcap.write(raw_data)
            eth = Ethernet(raw_data)

            #print(TAB_1 + 'Destination: {}, Source: {}, Protocol: {}'.format(eth.dest_mac, eth.src_mac, eth.proto))
            #print('\nEthernet Frame:')
            ipv4 = IPv4(eth.data) 
            ip_address = IP(ipv4.src)
            ip_type = ip_address.iptype()
            if ip_type == 'PRIVATE':
                if ipv4.src not in exception_ip:
                    if str(ipv4.ttl) not in exception_ttl:
                        if eth.proto == 8:
                            #print(TAB_1 + 'IPv4 Packet:')
                            #print(TAB_2 + 'Version: {}, Header Length: {}, TTL: {},'.format(ipv4.version, ipv4.header_length, ipv4.ttl))
                            #print(TAB_2 + 'Protocol: {}, Source: {}, Target: {}'.format(ipv4.proto, ipv4.src, ipv4.target))
                            WriteToSqlite(eth.src_mac, ipv4.src, 'windows')
        except KeyboardInterrupt:
            WriteToSqlite(eth.src_mac, ipv4.src, 'windows')
            time.sleep(5)
            print('>>>>>>>>>>>>>>>>>>>>>>>.save file.<<<<<<<<<<<<<<<<<<<<<<<<<<<<,,,')
            break
    pcap.close()

main()
