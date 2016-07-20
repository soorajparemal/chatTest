from socket import *

text=raw_input('Enter your message : ')

fd=socket(AF_INET,SOCK_DGRAM)

fd.sendto(str(text),('127.0.0.1',7000))

