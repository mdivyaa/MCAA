# Count Digits, Letters, Special Characters
text = input("Enter a string: ")
letters = digits = specials = 0

for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    else:
        specials += 1

print("Letters:", letters)
print("Digits:", digits)
print("Special characters:", specials)
