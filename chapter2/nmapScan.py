import nmap
import argparse
def nmapScan(tgtHost, tgtPort):
	nmScan = nmap.PortScanner()
	nmScan.scan(tgtHost, tgtPort)
	state=nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
	print " [*] " + tgtHost + " tcp/"+tgtPort +" "+state
def main():
	parser = argparse.ArgumentParser("usage%prog " "-H  <target host> -p <target port>")
	parser.add_argument('-H', '--tgtHost', type=str, help='specify target host')
	parser.add_argument('-p', '--tgtPort', nargs= '*', type=str, help='specify target port')
	args = parser.parse_args()
	tgtHost = args.tgtHost
	tgtPorts = args.tgtPort#str(args.tgtPort).split(', ')
	if (tgtHost == None) | (tgtPorts[0] == None):
		print parser.usage
		exit(0)
	for tgtPort in tgtPorts:
		nmapScan(tgtHost, tgtPort)
if __name__ == '__main__':
	main()
