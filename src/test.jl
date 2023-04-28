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
