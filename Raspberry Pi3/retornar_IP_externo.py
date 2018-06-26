from urllib2 import urlopen

ip = urlopen('http://ipecho.net/plain').read()

print(ip)