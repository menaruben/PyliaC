import ctypes
from subprocess import check_output
from os import system

class PyliaC:
    """
    PyliaC is an interface between Python and Julia written in C
    """
    def __init__(self, julia_file: str, julia_interpreter: str = "julia", c_path: str = "./pyliac") -> None:
        self.julia_file = julia_file
        self.julia_interpreter = julia_interpreter
        system(f"gcc -fPIC -shared -o {c_path}.so {c_path}.c")
        self.clib = ctypes.CDLL(f"{c_path}.so")
        self.functions = self.get_functions()
        self.declare_funcs()

    def get_functions(self):
        """
        parses out functions from the julia file
        """
        self.clib.get_functions.restype = ctypes.POINTER(ctypes.c_char_p)
        cstring_pointer = self.clib.get_functions(b'./test.jl')

        # get the array size by counting null-terminated strings
        array_size = 0
        while cstring_pointer[array_size]:
            array_size += 1

        # create a Python list and copy each string from the array
        function_list = []
        for i in range(array_size):
            function_string = cstring_pointer[i].decode("utf-8")
            function_name = function_string.split("(")
            function_list.append(function_name[0])

        return function_list

    def declare_funcs(self):
        """
        automatically declares functions according to self.functions
        """
        for function_name in self.functions:
            def func(self, args: list, fname=function_name):
                args_list = [str(num) for num in args]

                cmd = ([self.julia_interpreter, self.julia_file, fname] + args_list)
                output_str = check_output(cmd)

                output = output_str.strip().decode("utf-8")
                return output

            setattr(PyliaC, function_name.replace('-', '_'), func)
