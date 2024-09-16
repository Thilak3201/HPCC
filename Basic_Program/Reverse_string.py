# To reverse a string

l = input("Enter the string")
print(l[::-1])                        # slicing method


# join method with blank space

n = input("Enter the string using join")
print(''.join(reversed(n)))            # join and blank space using a rverse a string



# normal method

s = "data"
i = len(s)-1
result =''
while i >= 0 :
    result = result+s(i)
    i = i-1
print(result)