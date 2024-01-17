use std::error::Error;
use std::fs;
use serde::{Deserialize, Serialize};

#[derive(Debug, Deserialize, Serialize)]
pub struct ConnectApril;

impl ConnectApril {
    pub fn recv_request<T>() -> Result<T, Box<dyn Error>>
    where T: Deserialize<'static'>,
    {
        let n = std::env::args().last().expect("Please provide a command-line argument");
        let file_path = format!("./{}.input", n);

        let data = fs::read_to_string(file_path)?;
        let parsed_data = serde_json::from_str(&data)?;

        Ok(parsed_data)
    }

    pub fn send_response<T>(response: &T) -> Result<(), Box<dyn Error>>
    where T: Serialize,
    {
        let n = std::env::args().last().expect("Please provide a command-line argument");
        let file_path = format!("./{}.output", n);

        let response_json = serde_json::to_string_pretty(response)?;
        fs::write(file_path, response_json)?;

        Ok(())
    }
}

