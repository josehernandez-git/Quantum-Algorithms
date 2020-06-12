# -*- coding: utf-8 -*-
""



# This is an execution of the Fibonacci Sequence 



terms = int(input("How many terms would you like for me to go to?"))

Fib = [0,1]

x = 0

while x < terms:
    a = Fib[-1] + Fib[-2]
    Fib.append(a)
    x += 1 
print(Fib)

# to print not in a list
for n in Fib:
    print(n, end = " ")
    