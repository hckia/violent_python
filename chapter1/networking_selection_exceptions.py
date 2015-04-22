import socket 
#This script will print the banner after connecting to a specific IP address and TCP port.
#After importing the socket module, we insantiate a new variable s from the class socket.
#Next, we use the connect() method to make a network connection to the IP address and port
#Once successfully connected, we can read and write from the socket.
#the recv(1024) method will read the next 1024 bytes on the socket. We will store the result of this method in a variable then print the results to server

socket.setdefaulttimeout(2)
s = socket.socket()
try:
	s.connect(("173.236.253.220",21))
except Exception, e:
	print "[-] Shoot! Error = "+str(e)
banner = s.recv(1024)


#We would like to know if the specific FTP server is vulnerable to attack. To do this, we will compare our results against some known vulnerable FTP server versions
if("FreeFloat Ftp Server (Version 1.00)" in banner):
	print "[+] FreeFloat FTP Server is vulnerable."
elif("3Com 3CDaemon FTP Server Version 2.0" in banner):
	print "[+] 3CDaemon FTP server is vulnerable."
elif("Ability Server 2.34" in banner):
	print "[+] Ability FTP server is vulnerable."
elif("Sami FTP Server 2.0.2" in banner):
	print "[+] Sami FTP Server is vulnerable."
else:
	print "[-] FTP Server is not vulnerable."
