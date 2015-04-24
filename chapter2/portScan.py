import argparse

parser = argparse.ArgumentParser('usage %prog -H'  '<target host> -p <target port>')
parser.add_argument('-H', '--tgtHost', help='specify target host')
parser.add_argument('-p', '--tgtPort', help='specify target port')
args = parser.parse_args()

tgtHost = args.tgtHost
tgtPort = args.tgtPort

if (tgtHost == None) | (tgtPort == None):
	print parser.usage
	exit(0)
