s = "all the work is cool"
temp = s.split()
print(temp)
result = []
i = 0

while c < len(temp):
    if c not in result:
        result.append(c)
        i = i+1
print(result)