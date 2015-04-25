import argparse

def main():
        parser = argparse.ArgumentParser("usage%prog " "-H  <target host> -p <target port>")
        parser.add_argument('-H', '--tgtHost', help='specify target host')
        parser.add_argument('-p', '--tgtPort', nargs= '*', help='specify target port')
        args = parser.parse_args()
        tgtHost = args.tgtHost
        tgtPorts = str(args.tgtPort).split(' ')
        tgtPortsMapped = map(int, tgtPorts)
	print tgtPortsMapped
	#if (tgtHost == None) | (tgtPorts == None):
          #      print parser.usage
         #       exit(0)
        #portScan(tgtHost, tgtPorts)
if __name__ == '__main__':
        main()
