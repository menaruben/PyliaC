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

MyLib = PyliaC("~/Downloads/julia-1.8.3/bin/julia", # path to your julia interpreter
                "./test.jl",                        # path to your julia program
                "testlib.c"                         # path for the c code that will get compiled
                )

MyLib.lib.dotp(b"2 3 4 5")                          # output: 23.0
```

You will need to convert your arguments into bytes because the C code that gets generated when creating a new PyliaC`instance looks like this:
```C
#include <stdio.h>
#include <stdlib.h>


int add(char* args) {

    char cmd[1024];
    sprintf(cmd, "~/Downloads/julia-1.8.3/bin/julia ./test.jl add %s", args);
    system(cmd);
    return 0;
}


int multiply(char* args) {

    char cmd[1024];
    sprintf(cmd, "~/Downloads/julia-1.8.3/bin/julia ./test.jl multiply %s", args);
    system(cmd);
    return 0;
}


int greet(char* args) {

    char cmd[1024];
    sprintf(cmd, "~/Downloads/julia-1.8.3/bin/julia ./test.jl greet %s", args);
    system(cmd);
    return 0;
}


int dotp(char* args) {

    char cmd[1024];
    sprintf(cmd, "~/Downloads/julia-1.8.3/bin/julia ./test.jl dotp %s", args);
    system(cmd);
    return 0;
}
```
