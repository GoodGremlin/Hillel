import string

range = input("Enter a range (a-b):  ")

a, b = range.split("-")

leftPosition, rightPosition = string.ascii_letters.find(a), string.ascii_letters.find(b)

result = string.ascii_letters[leftPosition: rightPosition + 1]

print(result)