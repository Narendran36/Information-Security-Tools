from struct import *
packet = b'\x08\x00\x00\x00\xf6\x01\x00\x00\x24\x00\x00\x00\x03\x00\x00\x00\x0c\x00\x00\x00I think, therefore I am.\xca\xcd\x00\x00'

#### Don't change the code until this line ####

def show_details():
    pass # print sender ID (decimal), message ID (decimal), the actual message (readable english text), and its checksum (decimal)
    d_p = unpack('<5i23si',packet)
    print("sender ID ",d_p[0],", message ID ",dp[4],", the actual message ",d_p[5],", and its checksum ",d_p[6])
show_details()
