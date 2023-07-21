def pow(a, b):
    result = 1
    for i in range(b):
        result *= a
    return result
result = pow(2, 3)
print(result)  # Output: 8

result = pow(5, 2)
print(result)  # Output: 25

result = pow(10, -2)
print(result)  # Output: 0.01
