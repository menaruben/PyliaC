# PyliaC
PyliaC - an interface that opens the possibility to run your julia commands inside your python code.

# Example
The PyliaC is very similar to [Pylia](https://github.com/WoodyXP/Pylia). The difference is that it is not python that calls the functions but C. You will also need to use the [Fire](https://juliapackages.com/p/fire) in Julia in order to run it like a cli application. Here is an example on how you can build your julia file with the Fire package:
```julia
using Fire

@main function add(num::Integer...)
    println(sum(num))
end

@main function multiply(num::Integer...)
    println(prod(num))
end

@main function greet(name)
    println(name)
end

@main function dotp(nums::Integer...)
    vec1 = nums[1:(length(nums)/2)]
    vec2 = nums[((length(nums)/2)+1):length(nums)]

    dotproduct = 0.0
    i = 1
    while i <= length(vec1)
        dotproduct += vec1[i] * vec2[i]
        i += 1
    end
    println(dotproduct)
end
```

Now you can create a PyliaC instance inside your python code and start using the functions defined inside your ```test.jl``` file like this:
```python
from pyliac import PyliaC

juliaFile = PyliaC("./test.jl")

print(juliaFile.dotp([2, 3, 4, 5]))          # output: 23.0
```
