const ConnectApril = require('./connect_april'); // Assuming the JavaScript file is named 'April.js'

// Example usage:
const requestData = ConnectApril.recv_request();
console.log('Received data:', requestData);

const responseData = { output: 'Hello, World!' };
ConnectApril.send_response(responseData);
console.log('Response sent.');

