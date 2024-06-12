import string

phrase = input("Enter a phrase: ")

isPunctuation = any(char in string.punctuation for char in phrase)
length = len(phrase)


if length > 140:
    phrase = phrase[0:140]

if isPunctuation:
    for char in string.punctuation:
        phrase = phrase.replace(char, '')

phrase = f"#{phrase.title().replace(' ', '')}"


print(phrase)
print(isPunctuation)
