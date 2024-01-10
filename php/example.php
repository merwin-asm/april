<?php

require_once 'connect_april.php';

// Example usage:
$requestData = ConnectApril::recv_request();
echo 'Received data: ' . json_encode($requestData) . "\n";

$responseData = ['output' => 'Hello from, PHP!'];
ConnectApril::send_response($responseData);
echo "Response sent.\n";
?>

