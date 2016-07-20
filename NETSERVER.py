from socket import *

fd=socket(AF_INET,SOCK_DGRAM)

fd.bind(('127.0.0.1',7000))

text=fd.recvfrom(100)

print text
