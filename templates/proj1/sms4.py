









# @app.route('/AboutUS')
# def AboutUS():
#     return render_template('AboutUs.html')

# @app.route('/movieng/')
# def sendSMS(apikey, numbers, sender, message):
#     data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,'message' : message, 'sender': sender})
#     data = data.encode('utf-8')
#     request = urllib.request.Request("https://api.textlocal.in/send/?")
#     f = urllib.request.urlopen(request, data)
#     fr = f.read()
#     return(fr)
 
# resp =  sendSMS('MFCQ+xzrDwc-uRdIofMM0LlH4h9Gvj6j1tx3GqMHdq', '918605719895','TXTLCL', 'This is your message')
# print (resp)







[11:01 AM, 9/28/2019] Parvej SE: import urllib.request
import urllib.parse
 
@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/sendSMS')

def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)
 
resp =  sendSMS('J2rFg4JFJjA-JzgOEed4OSzgq85PEeCarh0zjw3vdd', '918605719895,917387148102',
    'TXTLCL', 'This is your message')
print (resp)




<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
<script type=text/javascript>
        $(function() {
          $('a#test').bind('click', function() {
            $.getJSON('/sendSMS',
                function(data) {
              console.log();
            });
            return false;
          });
        });
</script>
<head>

<link rel="stylesheet" type="text/css" href="/static/main.css">


</head>
<body>
 <form method="post">
<div id="main">
		<nav>
			<ul>
				<li><b><a href="/Home">Home</a></b></li>
				<li><b><a href="/Register">Register</a></b></li>
				<li><b><a href="/Login">Login</a></b></li>
				<li><b><a href="/AboutUs">About us</a></b></li>
				<li><b><a href="/ContactUs">Contact us</a></b></li>
				<!-- <li><b><a href="#">Dashboard</a></b></li> -->
			</ul>
		</nav>
</div>

       <div class="wrapper">
		<div class="parent" onclick="">
		<div class="child bg-one">
			 <a href=# id=test><button class='btn btn-default'>Shardanagar</button></a>
			//<p href="#" id ="test">Shardanagar</p>
			
		</div>
	</div>

	<div class="parent right" onclick="">
		<div class="child bg-two">
			
			<p href="#">Baramati</p>
			 
		</div>
	</div>


	<div class="parent" onclick="">
		<div class="child bg-three">
			<p href="#">Shardanagar</p>
			
		</div>
	</div>

	<div class="parent right" onclick="">
		<div class="child bg-four">
			
			<p href="#">Baramati</p>
			 
		</div>
	</div>

	
</div>
 </form>
</body>
