#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct April {
};

struct April* create_April() {
    struct April* april = (struct April*)malloc(sizeof(struct April));
    return april;
}

void destroy_April(struct April* april) {
    free(april);
}

char* recv_request() {
    char* n_str = strdup(getenv("ARGUMENT_VAR"));
    int n = atoi(n_str);
    free(n_str);

    char filename[20];
    sprintf(filename, ".%d.input", n);

    FILE* file = fopen(filename, "r");
    if (file == NULL) {
        perror("Error opening input file");
        exit(EXIT_FAILURE);
    }

    fseek(file, 0, SEEK_END);
    long file_size = ftell(file);
    fseek(file, 0, SEEK_SET);

    char* buffer = (char*)malloc(file_size + 1);
    fread(buffer, 1, file_size, file);
    fclose(file);

    buffer[file_size] = '\0';

    return buffer;
}

void send_response(char* response) {
    char* n_str = strdup(getenv("ARGUMENT_VAR"));
    int n = atoi(n_str);
    free(n_str);

    char filename[20];
    sprintf(filename, ".%d.output", n);

    FILE* file = fopen(filename, "w");
    if (file == NULL) {
        perror("Error opening output file");
        exit(EXIT_FAILURE);
    }

    fprintf(file, "%s", response);
    fclose(file);
}
