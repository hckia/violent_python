import argparse
import socket

def connScan(tgtHost, tgtPort):
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.connect((tgtHost, tgtPort))
		print '[+]%d/tcp open'% tgtPort
		conn.Skt.close()
	except:
		print '[-]%d/tcp close'% tgtPort
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
		print 'Scanning port ' + tgtPort
		connScan(tgtHost, int(tgtPort))
