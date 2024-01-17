// april.dart

import 'dart:convert';
import 'dart:io';

class ConnectApril {
  static Map<String, dynamic>? recvRequest() {
    final n = int.parse(Platform.args.last!);
    final filePath = '.$n.input';

    try {
      final data = File(filePath).readAsStringSync();
      return json.decode(data);
    } catch (e) {
      print('Error reading file: $filePath');
      return null;
    }
  }

  static void sendResponse(Map<String, dynamic> response) {
    final n = int.parse(Platform.args.last!);
    final filePath = '.$n.output';

    try {
      File(filePath).writeAsStringSync(json.encode(response));
    } catch (e) {
      print('Error writing file: $filePath');
    }
  }
}

