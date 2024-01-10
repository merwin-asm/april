#include "connect_april.h"
#include <stdio.h>
#include <stdlib.h>

json_t* recv_request(void) {
    const char* n = getenv("ARGUMENT");
    if (n == NULL) {
        fprintf(stderr, "Please provide a command-line argument\n");
        exit(EXIT_FAILURE);
    }

    char file_path[20];
    snprintf(file_path, sizeof(file_path), "./%s.input", n);

    FILE* file = fopen(file_path, "r");
    if (file == NULL) {
        fprintf(stderr, "Error reading file: %s\n", file_path);
        exit(EXIT_FAILURE);
    }

    fseek(file, 0, SEEK_END);
    long length = ftell(file);
    fseek(file, 0, SEEK_SET);

    char* data = (char*)malloc(length + 1);
    if (data == NULL) {
        fclose(file);
        fprintf(stderr, "Memory allocation error\n");
        exit(EXIT_FAILURE);
    }

    fread(data, 1, length, file);
    fclose(file);

    data[length] = '\0';
    json_t* json_data = json_loads(data, 0, NULL);
    free(data);

    return json_data;
}

void send_response(json_t* response) {
    const char* n = getenv("ARGUMENT");
    if (n == NULL) {
        fprintf(stderr, "Please provide a command-line argument\n");
        exit(EXIT_FAILURE);
    }

    char file_path[20];
    snprintf(file_path, sizeof(file_path), "./%s.output", n);

    FILE* file = fopen(file_path, "w");
    if (file == NULL) {
        fprintf(stderr, "Error writing file: %s\n", file_path);
        exit(EXIT_FAILURE);
    }

    char* response_str = json_dumps(response, JSON_INDENT(2));
    fprintf(file, "%s", response_str);
    fclose(file);
    free(response_str);
}

