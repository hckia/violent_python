import zipfile
import argparse 
#updated textbooks optparse since it's deprecated.
from threading import Thread

def extractFile(zFile, password):
	try:
		zFile.extractall(pwd=password)
		print '[+] Found password ' + password + '\n'
	except:
		pass
def main():
	parser = argparse.ArgumentParser("usage%prog " "-f <zipfile> -d <dictionary>")
	parser.add_argument('-f','--zname', help='specify zip file')
	parser.add_argument('-d', '--dname',  help='specify dictionary file')
	args = parser.parse_args()
	if (args.zname == None) | (args.dname == None):
		print parser.usage
		exit(0)
	else:
		zname = args.zname
		dname = args.dname
	zFile = zipfile.ZipFile(zname)
	passFile = open(dname)
	for line in passFile.readlines():
		password = line.strip('\n')
		t = Thread(target=extractFile, args=(zFile, password))
		t.start()
if __name__ == '__main__':
	main()
