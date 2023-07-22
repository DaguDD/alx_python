#!/usr/bin/env python3
def pow(a, b):
    result = 1
    for i in range(b):
        result *= a
    return result
result = pow(2, 3)
print(result)  

result = pow(5, 2)
print(result)  

result = pow(10, -2)
print(result)  
