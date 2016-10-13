from socket import*
fd=socket(AF_INET,SOCK_DGRAM)
fd.bind(('127.0.0.1',7000))
text=fd.recvfrom(100)
print text
a = list(text[1])
b=a[1]

fd.sendto(str('Response from server!'),('127.0.0.1',int(b)))

