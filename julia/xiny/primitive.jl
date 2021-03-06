# primitive datatypes and operators

# everything in julia is an expression

# basic types of numbers
println(typeof(3)) # Int64
println(typeof(3.2)) # Float64
println(typeof(2 + 1im)) # 1 and im. Complex{Int64}
println(typeof(2 // 3)) # Rational{Int64}

println(1 + 1)
println(div(5,2))
println(5 \ 35) # left division: weird notation.
println(2 ^ 2)
println(12 % 10)
# julia has integer under/overflow
println(10^19)
println(big(10)^19)
println(1e19)

# strings are utf-8 encoded. if they contain only ASCII,
# they can be changed and indexed. this is a lazy and safe by julia
ascii("this is a string")
