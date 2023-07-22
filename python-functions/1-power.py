#!/usr/bin/env python3
def pow(a, b):
    result = 1
    for i in range(b):
        result *= a
    return result
result = pow(2, 2)
print(result)  

result = pow(98, 2)
print(result)


result = pow(98, 0)
print(result)

result = pow(100, -2)
print(result)

result = pow(-4, 5)
print(result)
