# Attempting to download some jpg files from a website!
# Then create a JSON maybe?

from socket import *
import sys
import zlib

# Set up socket and URL
url="www.hoopshype.com"
nbasock = socket(AF_INET, SOCK_STREAM)
nbasock.settimeout(10)
nbasock.connect((url,80))

f=open('datasrc/players.txt','r')
htmlfd=open('meh.html','w')
temp=open('temp.txt','wb')
i=0
f2.write('<!DOCTYPE html><html>')
f2.write('<body>')

li=f.readline()[9:].rsplit('"')
filename=li[0]
imgfilename=filename[8:-4]+".jpg"
personname=imgfilename[1:-4].rsplit('_')
firstname=personname[0]
lastname=personname[1]
print(imgfilename)
print("we are looking for "+firstname+" "+lastname)

# request is the HTTP request being sent to the server
request = "GET "+filename+" HTTP/1.1\r\n\
Host: hoopshype.com\r\n\
Connection: keep-alive\r\n\
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n\
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36\r\n\
Accept-Language: en-US,en;q=0.8,ko;q=0.6,ja;q=0.4\r\n\r\n"
#Accept-Encoding: gzip, deflate, sdch\r\n\
#omg this line ^

#print (request)
brequest=request.encode() 	# convert unicode string to binary
nbasock.send(brequest)		# then send to the server!
#li='<a href="http://hoopshype.com'+li[0]+'">Player</a>\n'

while 1:
	try:
		nbasock.settimeout(.3)
		response=nbasock.recv(1024)
		
		#if response.len<6:
		#	break
		temp.write(response)
	
	except BaseException as e:
		print(e)
		break
#f2.write(li)
	
f.close()
temp.close()


f3=open("temp.txt",'r',encoding='UTF-8', newline='')
while 1:
	try:
		what=f3.readline()
		if imgfilename in what:
			#print(what[126:])
			pathArr=what[126:].rsplit('"')
			path=pathArr[0]
			break
	except BaseException as e:
		print(e)
		break

print(path)


htmlfd.write('</body></html>')
htmlfd.close()