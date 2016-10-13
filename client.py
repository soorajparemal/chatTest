from socket import*
text=raw_input("Enter 'Hi' : ")
fd=socket(AF_INET,SOCK_DGRAM)
fd.sendto(str(text),('127.0.0.1',7000))
resp=fd.recvfrom(100)
a= list(resp)
print 'Response from server : ' , a[0]
