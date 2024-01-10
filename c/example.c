#include "connect_april.h"
#include <stdio.h>

int main(int argc, char* argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <argument>\n", argv[0]);
        return EXIT_FAILURE;
    }

    // Set the environment variable for the argument
    setenv("ARGUMENT", argv[1], 1);

    // Example usage:
    json_t* request_data = recv_request();
    printf("Received data:\n%s\n", json_dumps(request_data, JSON_INDENT(2)));
    json_decref(request_data);

    // Assuming you have a JSON object to send as a response
    json_t* response_data = json_object();
    json_object_set_new(response_data, "output", json_string("Hiii!"));
    send_response(response_data);
    json_decref(response_data);

    return EXIT_SUCCESS;
}

