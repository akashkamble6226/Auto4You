import urllib.request
import urllib.parse
 
username = 'Parvej'
 
apihash = 'dgDpU4wgcrk-UfUgKP7CLLl28GHbIP3Vl5vlrBeah6'
 
sender = 'RPiSpy'
 

test_flag = 1
 

numbers = ('918605719895,917387148102')
 

message = 'Test message sent from my Raspberry Pi'
 
 
values = {'test'    : test_flag,
          'username': username,
          'hash'    : apihash,
          'message' : message,
          'sender'  : sender,
          'numbers' : numbers }
 
url = 'https://api.txtlocal.com/send/'
 
postdata = urllib.urlencode(values)
req = urllib2.Request(url, postdata)
 
print('Attempt to send SMS ...')
 
try:
  response = urllib2.urlopen(req)
  response_url = response.geturl()
  if response_url==url:
    print('SMS sent!')
