import urllib.request
import urllib.parse
 
def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)
 
resp =  sendSMS('J2rFg4JFJjA-QR1t1LBlWyc4MRPfTAqxZ7pVcFJhjm', '918605719895,917387148102',
    'TXTLCL', 'just Done')
print (resp)
print("message sent static")