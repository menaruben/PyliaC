from ctypes import CDLL
from os import system

class PyliaC:
    def __init__(self, julia_interpreter: str, julia_file: str, c_path: str) -> None:
        self.julia_interpreter = julia_interpreter
        self.julia_file = julia_file
        self.c_path = c_path
        self.c_so_path = self.c_path.replace(".c", ".so")
        self.functions = self.get_functions()
        self.julia_funcs_to_c()
        self.compile_c_to_so()
        self.lib = CDLL(f"./{self.c_so_path}")

    def get_functions(self) -> list:
        functions = []
        with open(self.julia_file, "r") as file:
            file.readlines

            for line in file:
                if line.startswith("@main function "):
                    function = (line.replace("@main function ", "").replace("\n", "")).split("(")
                    functions.append(function[0])

        return functions

    def julia_funcs_to_c(self) -> None:
        with open(self.c_path, "w", encoding="utf-8") as file:
            headers = """#include <stdio.h>
#include <stdlib.h>

"""
            file.writelines(headers)
            for func in self.functions:
                code = f"""
int {func}(char* args) {{

    char cmd[1024];
    sprintf(cmd, "{self.julia_interpreter} {self.julia_file} {func} %s", args);
    system(cmd);
    return 0;
}}

"""
                file.writelines(code)

    def compile_c_to_so(self) -> None:
        system(f"gcc -fPIC -shared -o {self.c_so_path} {self.c_path}")

MyLib = PyliaC("~/Downloads/julia-1.8.3/bin/julia", "./test.jl", "testlib.c")
MyLib.lib.greet(b"rubi")
