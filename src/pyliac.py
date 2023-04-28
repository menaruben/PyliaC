import os
import ctypes

path = os.getcwd()
clib = ctypes.CDLL(os.path.join(path, "pyliac.so"))

class PyliaC:
    def __init__(self, file_path: str, julia_interpreter: str = "julia") -> None:
        self.file_path = file_path
        self.julia_interpreter = julia_interpreter
        self.functions = Julia().get_function_list(bytes(file_path, "utf-8"))

    def call_func(self, function_name: bytes, args: bytes):
        clib.call(bytes(self.julia_interpreter, "utf-8"), function_name, args)

class Julia(ctypes.Structure):
    _fields_ = [
                ("file_path", ctypes.c_char_p),
                ("functions", ctypes.POINTER(ctypes.c_char_p))]

    def get_function_list(self, file_path: bytes) -> list:
        clib.Julia_init.restype = ctypes.POINTER(Julia)
        julia_file = clib.Julia_init(file_path)

        function_list = []
        func = julia_file.contents.functions[0]
        while func is not None:
            function_list.append((func.decode().split("("))[0])
            func = julia_file.contents.functions[len(function_list)]

        return function_list
