import argparse
from socket import *
from threading import *

screenLock = Semaphore(value=1)
def connScan(tgtHost, tgtPort):
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.connect((tgtHost, tgtPort))
		connSkt.send('ViolentPython\r\n')
		results = connSkt.recv(100)
		screenLock.acquire()
		print '[+]%d/tcp open for port '% tgtPort
		print '[+] ' + str(results)
	except:
		screenLock.acquire()
		print '[-]%d/tcp closed for port '% tgtPort
	finally:
		screenLock.release()
		connSkt.close()
def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print "[-] Cannot resolve '%s': Unknown host"%tgtHost
		return
	try:
		tgtName = gethostbyaddr(tgtIP)
		print '\n[+] Scan results for: ' + tgtName[0]
	except:
		print '\n[+] Scan Results for: ' + tgtIP
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t = Thread(target=connScan, args=(tgtHost, tgtPort))
		t.start()
def main():
	parser = argparse.ArgumentParser("usage%prog " "-H  <target host> -p <target port>")
	parser.add_argument('-H', '--tgtHost', help='specify target host')
	parser.add_argument('-p', '--tgtPort', nargs= '*', type=int, help='specify target port')
	args = parser.parse_args()
	tgtHost = args.tgtHost
	tgtPorts = args.tgtPort
	if (tgtHost == None) | (tgtPorts == None):
		print parser.usage
		exit(0)
	portScan(tgtHost, tgtPorts)
if __name__ == '__main__':
	main()
