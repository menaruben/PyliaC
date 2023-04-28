#include <stdio.h>
#include <stdlib.h>

int greet(char* name) {
    printf("Hello %s!\n (C)", name);
    return 0;
}

int greet2(char* julia_interpreter) {

    char cmd[100];
    sprintf(cmd, "%s test.jl add 1 2 3", julia_interpreter);
    system(cmd);
    return 0;
}
