#lets declare variables
port = 21 # An integer
print str(type(port))
banner = "FreeFloat FTP Server" # A string
print str(type(banner))
portList=[21,22,80,110] # a list
print str(type(portList))
portOpen = True # A boolean
print str(type(portOpen))

#lets print a full String
print "[+] Checking for "+banner+" on port "+str(port)

#lets manipulate some variables
print banner.upper()+"\n"
print banner.lower()+"\n"
print banner.replace('FreeFloat','Ability')
print str(banner.find('FTP'))+"th offset where the FTP string occurs.\n"

#lets show the position of port 21 in portList
pos = portList.index(21)
print "Port 21 is in position "+str(pos)+".\n"

#lets remove everything from portList
portList.remove(21)
portList.remove(22)
portList.remove(80)
portList.remove(110)
#lets put them back in the opposite order.
portList.append(110)
portList.append(80)
portList.append(22)
portList.append(21)

#lets check position 21 again. 
print "Port 21 is in position "+str(pos)+".\n"

#lets show off our array
print portList

#How many ports are there?
cnt = len(portList)
print "Scanning "+str(cnt)+" total ports.\n"
