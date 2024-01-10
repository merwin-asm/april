#include "connect_april.h"
#include <fstream>
#include <iostream>

nlohmann::json ConnectApril::recv_request() {
    const char* n = std::getenv("ARGUMENT");
    if (n == nullptr) {
        std::cerr << "Please provide a command-line argument" << std::endl;
        std::exit(EXIT_FAILURE);
    }

    std::string file_path = "./" + std::string(n) + ".input";
    std::ifstream file(file_path);
    
    if (!file.is_open()) {
        std::cerr << "Error reading file: " << file_path << std::endl;
        std::exit(EXIT_FAILURE);
    }

    nlohmann::json json_data;
    file >> json_data;
    return json_data;
}

void ConnectApril::send_response(const nlohmann::json& response) {
    const char* n = std::getenv("ARGUMENT");
    if (n == nullptr) {
        std::cerr << "Please provide a command-line argument" << std::endl;
        std::exit(EXIT_FAILURE);
    }

    std::string file_path = "./" + std::string(n) + ".output";
    std::ofstream file(file_path);
    
    if (!file.is_open()) {
        std::cerr << "Error writing file: " << file_path << std::endl;
        std::exit(EXIT_FAILURE);
    }

    file << std::setw(2) << response;
}

