from socket import*
fd=socket(AF_INET,SOCK_DGRAM)
fd.bind(('127.0.0.1',7000))
text=list(fd.recvfrom(100))
a = text[1]

b=a[1]

print 'Recieved a text : "' + str(text[0]) +'" from port : '+str(b) 

fd.sendto(str('Hi there !'),('127.0.0.1',int(b)))

