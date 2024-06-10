import string
import keyword

nameOfVariable = input("Enter your variable name: ")

# - будет ли данный способ более эффективным нежеле работа со строкой которая ниже?
# punctuationSing = set(string.punctuation) - set('_')

punctuationSing = string.punctuation.replace('_', '')

kwlist = keyword.kwlist

isCorrectSing = not any(char in punctuationSing for char in nameOfVariable) and \
                ('__' not in nameOfVariable and '___' not in nameOfVariable)

isNoSpaces = ' ' not in nameOfVariable

isNotReserveWord = nameOfVariable not in kwlist

isDigit = nameOfVariable[0].isdigit()
isLowerCase = all(char.islower() for char in nameOfVariable if char.isalpha())

isCorrectName = isCorrectSing and isNoSpaces and isNotReserveWord and not isDigit and isLowerCase


print("isCorrectName:", isCorrectName)
