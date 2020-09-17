import socket

ip = input("Enter the IP address: ")
port = input("Enter the port number: ")
port = int(port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if sock.connect_ex((ip,port)):
        print("Port ",port," is closed")
else:
        print("Port ",port," is open")
