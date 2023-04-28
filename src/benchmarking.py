from pyliac import PyliaC
import time

MyLib = PyliaC("~/Downloads/julia-1.8.3/bin/julia", "./test.jl", "testlib.c")

def get_average_runtime(num_of_tests: int, byte_args: bytes) -> float:
    runtimes = []
    for _ in range(num_of_tests):
        start_time = time.time()
        MyLib.lib.dotp(byte_args)
        end_time = time.time()
        runtimes.append(end_time - start_time)

    runtime_sum = 0.0
    for runtime in runtimes:
        runtime_sum += runtime

    return runtime_sum/num_of_tests

b_args = b"2 3 4 5"
print(f"The average runtime for the dotp function was: {get_average_runtime(10, bargs)} seconds")
