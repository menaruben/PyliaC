from pyliac import PyliaC
import time

juliaFile = PyliaC("./test.jl")

def get_average_runtime(num_of_tests: int, byte_args: bytes) -> float:
    runtimes = []
    for _ in range(num_of_tests):
        start_time = time.time()
        juliaFile.dotp([22, 37, 46, 54, 66, 235])
        end_time = time.time()
        runtimes.append(end_time - start_time)

    runtime_sum = 0.0
    for runtime in runtimes:
        runtime_sum += runtime

    return runtime_sum/num_of_tests

b_args = b"2 3 4 5"
print(f"The average runtime for the dotp function was: {get_average_runtime(10, b_args)} seconds")