// main.ts

import { ConnectApril } from './connect_april';

// Example usage:
const requestData = ConnectApril.recv_request();
console.log('Received data:', requestData);

const responseData = { output: 'Hello, World!' };
ConnectApril.send_response(responseData);
console.log('Response sent.');

