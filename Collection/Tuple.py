# tuple is a immutable and once tuple is assigned we can not edit and update
# it allows duplicates
# tuple is used pranthasis >()

tpl = (10,20,30, "arun", 10)

print(tpl)

print(tpl[0:3])

print(tpl.count(10))

print((10) in tpl)  # Here checking 10 avalilable in tpl


# Convert list to tuple

lst = [23,45,56,67]
tpl2 = tuple(lst)
print(tpl2)
print(type(tpl2))
