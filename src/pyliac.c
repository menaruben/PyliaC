#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Julia {
    char* file_path;
    char** functions;
};

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

// void split_at(char* string, char* separator) {
//     char* piece = strtok(string, separator);
//     while (piece != NULL) {
//         printf("%s\n", piece);
//         piece = strtok(NULL, separator);
//     }
// }

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

            // extract function name
            char* open_paren = strchr(function_name, '('); // get first occurence
            if (open_paren != NULL) {
                // allocate buffer for function name
                int name_len = open_paren - function_name;
                char* func_name = malloc((name_len + 1) * sizeof(char));
                strncpy(func_name, function_name, name_len);
                func_name[name_len] = '\0';

                // add function name to list
                functions[i] = func_name;
                i++;
            }
        }

        // get the next line
        lines = strtok(NULL, "\n");
    }

    free(file_content);
    functions[i] = NULL;
    return functions;
}

// Define a custom constructor for the Julia struct
struct Julia* Julia_init(char* file_path) {
    struct Julia* julia = malloc(sizeof(struct Julia));
    julia->file_path = file_path;
    julia->functions = get_functions(file_path);
    return julia;
}

// call function
void call(char* julia_interpreter, char* function_name, char* args) {

    char cmd[1024];
    sprintf(cmd, "%s ./test.jl %s %s", julia_interpreter, function_name, args);
    system(cmd);
}
