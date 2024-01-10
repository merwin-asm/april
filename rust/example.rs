use connect_april::ConnectApril;

#[derive(Debug, serde::Deserialize, serde::Serialize)]
struct RequestData {
    // Define your fields here
    field1: String,
    field2: i32,
}

#[derive(Debug, serde::Deserialize, serde::Serialize)]
struct ResponseData {
    message: String,
}

fn main() {
    // Example usage:
    let request_data: RequestData = ConnectApril::recv_request().expect("Error receiving data");
    println!("Received data: {:#?}", request_data);

    // Assuming you have a struct to send as a response
    let response_data = ResponseData {
        message: format!("Hello from, Rust! Received: {:?}", request_data),
    };

    ConnectApril::send_response(&response_data).expect("Error sending response");
    println!("Response sent.");
}

