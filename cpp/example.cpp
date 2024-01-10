#include "connect_april.h"
#include <iostream>

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <argument>" << std::endl;
        return EXIT_FAILURE;
    }

    // Set the environment variable for the argument
    std::string argument = argv[1];
    setenv("ARGUMENT", argument.c_str(), 1);

    // Example usage:
    nlohmann::json request_data = ConnectApril::recv_request();
    std::cout << "Received data:\n" << std::setw(2) << request_data << std::endl;

    // Assuming you have a JSON object to send as a response
    nlohmann::json response_data = {{"output", "Hello, C++"}};
    ConnectApril::send_response(response_data);
    std::cout << "Response sent." << std::endl;

    return EXIT_SUCCESS;
}

