
# Palindrome Check (Case-Insensitive)
text = input("Enter a word or number: ").lower()

if text == text[::-1]:
    print("It is a Palindrome")
else:
    print("It is Not a Palindrome")
