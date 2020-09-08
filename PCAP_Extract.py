from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment

#### Don't change the code until this line ####

def show_mac_address():
    packets = rdpcap(recording_path)
    for packet in packets:
        print(packet.src)
    pass # print mac address

show_mac_address()
