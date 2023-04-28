from pyliac import *

juliaFile = PyliaC("./test.jl")

greet_output = juliaFile.greet(["Rubi"])
dotp_output = juliaFile.dotp([2, 3, 4, 5])

print(greet_output, dotp_output)