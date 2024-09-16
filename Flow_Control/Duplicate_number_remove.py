# Remove duplicates
# The Python eval() is a built-in function that allows us to evaluate the Python expression as a 'string' and return the value as an integer.

l1 = eval(input("Enter the number"))
print(l1)
l2 = []
for each_value in l1:
     if each_value not in l2 :
         l2.append(each_value)

print(l2)


# One more method (set is not allowed duplicate values )

l1 = eval(input("Enter the number "))
s1 = set(l1)
print(s1)

