output = ""
for i in range(10):
    for j in range(i+1, 10):
        output += "{:02d}, {:02d}, ".format(i, j)
print(output[:-2])
