from pyliac import PyliaC
import time

juliaFile = PyliaC("./test.jl")

def get_average_runtime(num_of_tests: int, function_name:bytes, byte_args: bytes) -> float:
    runtimes = []
    for _ in range(num_of_tests):
        start_time = time.time()
        juliaFile.call_func(function_name, byte_args)
        end_time = time.time()
        runtimes.append(end_time - start_time)

    runtime_sum = 0.0
    for runtime in runtimes:
        runtime_sum += runtime

    return runtime_sum/num_of_tests

b_fname = b"dotp"
b_args = b"1 2 3 4 5 6"
print(f"The average runtime for the dotp function was: {get_average_runtime(20, b_fname, b_args)} seconds")