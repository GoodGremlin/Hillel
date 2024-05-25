
numbers = int(input())

leftPart, rightPart = divmod(numbers, 100)

firstNumber, secondNumber = divmod(leftPart, 10)
thirdNumber, fourthNumber = divmod(rightPart, 10)


print(firstNumber)
print(secondNumber)
print(thirdNumber)
print(fourthNumber)
