const fs = require('fs');

class ConnectApril {
  static recv_request() {
    const n = process.argv[2];
    const filePath = `.${n}.input`;

    try {
      const data = fs.readFileSync(filePath, 'utf8');
      return JSON.parse(data);
    } catch (err) {
      console.error(err);
      return null;
    }
  }

  static send_response(response) {
    const n = process.argv[2];
    const filePath = `.${n}.output`;

    try {
      fs.writeFileSync(filePath, JSON.stringify(response));
    } catch (err) {
      console.error(err);
    }
  }
}
