
# Find the maximum of three numbers without max()
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    max_num = a
elif b > c:
    max_num = b
else:
    max_num = c

print("The largest number is:", max_num)
