def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
result = convert_to_celsius(32)
print(result)  # Output: 0.0

result = convert_to_celsius(68)
print(result)  # Output: 20.0

result = convert_to_celsius(100)
print(result)  # Output: 37.77777777777778
