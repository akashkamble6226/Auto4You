<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>abc</title>
</head>
<body>


<button type="button">submit</button>




</body>
</html>




<?php

if(isset($_POST["submit"]))
 { 
    
     
   // Account details
	$apiKey = urlencode('Zro10KL6WX4-JLonhn7ZWL3EKizytkAqKTlafsv6mO');
	{% csrf_token %}
	// Message details
	$numbers = array(918605719895);
	$sender = urlencode('TXTLCL');
	$message = rawurlencode('this is php');
 
	$numbers = implode(',', $numbers);
 
	// Prepare data for POST request
	$data = array('apikey' => $apiKey, 'numbers' => $numbers, "sender" => $sender, "message" => $message);
 
    // Send the POST request with cURL
    
	$ch = curl_init('https://api.textlocal.in/send/');
	curl_setopt($ch, CURLOPT_POST, true);
	curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	$response = curl_exec($ch);
	curl_close($ch);
	
	// Process your response here
	echo $response;


}
	
?>