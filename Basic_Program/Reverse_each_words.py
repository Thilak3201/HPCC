# Write a program  to reverse a each string

n = "python is cool"
temp = n.split()                        # using slipt method to sequence the string
print(temp)
result = []
i = 0

while i<len(temp):
    result.append(temp[i][::-1])
    i = i+1
print(result)
output = ' '.join(result)      # converted sequence back to string using delimter of empty space $join method
print(output)

