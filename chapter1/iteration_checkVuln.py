import socket

def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return banner
	except:
		return
def checkVulns(banner):
	if '' in banner:
		
	elif '' in banner:
		
	elif '' in banner:
		
	elif '' in banner:
		
	else:
		
	return
def main():
	portList = [21,22,25,80,110,443]
	for x in range(1, 255)
		for port in portList:
			banner = retBanner(ip, port)
			if banner:
				print '[+] '+ ip + ': ' + banner
				checkVulns(banner)
if __name__ == '__main__':
	main()
