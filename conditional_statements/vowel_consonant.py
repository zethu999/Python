"""Check the letter is vowel or consonant"""

letter = input("Enter a letter: ")

if(letter.lower() == "a" or letter.lower() == "e" or letter.lower() == "i" or letter.lower() == "o" or letter.lower() == "u") :
    print("Vowel")
else :
    print("Consonant")