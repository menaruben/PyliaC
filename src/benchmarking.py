from pyliac import PyliaC
import time

juliaFile = PyliaC("./test.jl")

def get_average_runtime(num_of_tests: int, byte_args: list) -> float:
    runtimes = []
    for _ in range(num_of_tests):
        start_time = time.time()
        juliaFile.dotp(byte_args)
        end_time = time.time()
        runtimes.append(end_time - start_time)

    runtime_sum = 0.0
    for runtime in runtimes:
        runtime_sum += runtime

    return runtime_sum/num_of_tests

b_args = [2242, 3741, 4643, 5466, 6106, 6235]
print(f"The average runtime for the dotp function was: {get_average_runtime(10, b_args)} seconds")