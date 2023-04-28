#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* get_content(char* path) {

    FILE* file_ptr;
    char ch;
    char* file_content = NULL;
    long file_size;

    // open file in reading mode
    file_ptr = fopen(path, "r");

    // get file size
    fseek(file_ptr, 0, SEEK_END);
    file_size = ftell(file_ptr);
    fseek(file_ptr, 0, SEEK_SET);

    // allocate memory for file content
    file_content = malloc(file_size + 1);

    // read file content
    int i = 0;
    while ((ch = fgetc(file_ptr)) != EOF) {
        file_content[i] = ch;
        i++;
    }
    file_content[i] = '\0';

    fclose(file_ptr);
    return file_content;
    free(file_content);
}

_Bool starts_with(const char *pre, const char *str) {
    return strncmp(pre, str, strlen(pre)) == 0;
}

char** get_functions(char* file_path) {

    // make copy of file content string (strtok modifies the input string)
    char* file_content = get_content(file_path);
    char** functions = malloc(1024 * sizeof(char*));

    // "tokenize" file content based on newline char
    char* lines = strtok(file_content, "\n");
    int i = 0;

    while (lines != NULL) {
        // if line starts with "@main function" extract the function name
        if (starts_with("@main function ", lines)) {
            // skip "@main function" prefix
            char* function_name = lines + strlen("@main function ");
            char* end = function_name + strlen(function_name) - 1;

            // add function name to list
            functions[i] = function_name;
            i++;
        }

        // get the next line
        lines = strtok(NULL, "\n");
    }

    free(file_content);
    functions[i] = NULL;
    return functions;
}

// int main() {
//     char** functions = get_functions("./test.jl");
//     for (int i = 0; functions[i] != NULL; i++) {
//         printf("%s\n", functions[i]);
//     }

//     free(functions);
//     return 0;
// }
