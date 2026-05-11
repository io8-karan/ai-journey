# vowel or consonant (wrong way - for learning)

char = input("Enter a character: ")
if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
    print("char is vowel")
else:
    print("char is consonant")

#wrong approach
# right way

char = str(input("Enter a character: "))
if len(char) == 1 and char.isalpha():
    if char.lower() in 'aeiou':
        print("char is vowel")
    else:
        print("char is consonant")
else:
    print("Invalid input. Please enter a single alphabetic character.")
