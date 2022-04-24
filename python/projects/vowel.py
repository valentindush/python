n = input('Enter a letter of your choice: ')

if n in ['a', 'i', 'u', 'o', 'e'] or n in ['A', 'I', 'U', 'O', 'E']:
    print(n, "is a vowel")
elif n == 'y' or n == 'Y':
    print(n, "is either a vowel or consonant")
else:
    print(n, " is a consonant")
