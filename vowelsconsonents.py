#Counting Vowels and Consonents in a String
text = input("Enter a string: ").lower()

vowels = "aeiou"
vowel_count = consonant_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            print(char, "→ Vowel")
            vowel_count += 1
        else:
            print(char, "→ Consonant")
            consonant_count += 1

print("\nTotal Vowels:", vowel_count)
print("Total Consonants:", consonant_count)
