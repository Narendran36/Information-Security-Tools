from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment
import re

#### Don't change the code until this line ####

def show_username_password():
    bind_layers( TCP, HTTP, sport=8000 )
    bind_layers( TCP, HTTP, dport=8000 )
    packets = rdpcap(recording_path)
    pattern = 'username=(.*)&password=([^\s]+)'
    for packet in packets:
        content = raw(packet[HTTP]).decode('ascii')
        match = re.search(pattern,content)
        if match:
            print(match.group(0))
        
show_username_password()
