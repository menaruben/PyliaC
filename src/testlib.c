#include <stdio.h>
#include <stdlib.h>


int add(char* args) {

    char cmd[1024];
    sprintf(cmd, "C:/Users/ruben/AppData/Local/Programs/Julia-1.8.3/bin/julia.exe ./test.jl add %s", args);
    system(cmd);
    return 0;
}


int multiply(char* args) {

    char cmd[1024];
    sprintf(cmd, "C:/Users/ruben/AppData/Local/Programs/Julia-1.8.3/bin/julia.exe ./test.jl multiply %s", args);
    system(cmd);
    return 0;
}


int greet(char* args) {

    char cmd[1024];
    sprintf(cmd, "C:/Users/ruben/AppData/Local/Programs/Julia-1.8.3/bin/julia.exe ./test.jl greet %s", args);
    system(cmd);
    return 0;
}


int dotp(char* args) {

    char cmd[1024];
    sprintf(cmd, "C:/Users/ruben/AppData/Local/Programs/Julia-1.8.3/bin/julia.exe ./test.jl dotp %s", args);
    system(cmd);
    return 0;
}

