// main.dart

import 'april.dart';

void main() {
  // Example usage:
  final requestData = ConnectApril.recvRequest();
  print('Received data: $requestData');

  final responseData = {'output': 'Hello from, Dart!'};
  ConnectApril.sendResponse(responseData);
  print('Response sent.');
}

