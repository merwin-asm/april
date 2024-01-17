import * as fs from 'fs';

class ConnectApril {
  static recv_request(): any | null {
    const n: string = process.argv[process.argv.length-1];
    const filePath: string = `.${n}.input`;

    try {
      const data: string = fs.readFileSync(filePath, 'utf8');
      return JSON.parse(data);
    } catch (err) {
      console.error(err);
      return null;
    }
  }

  static send_response(response: any): void {
    const n: string = process.argv[process.argv.length-1];
    const filePath: string = `.${n}.output`;

    try {
      fs.writeFileSync(filePath, JSON.stringify(response));
    } catch (err) {
      console.error(err);
    }
  }
}

// Example usage:
//const requestData = ConnectApril.recv_request();
//console.log('Received data:', requestData);

//const responseData = { output: 'Hello, World!' };
//ConnectApril.send_response(responseData);
//console.log('Response sent.');

