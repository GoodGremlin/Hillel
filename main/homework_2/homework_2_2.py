numbers = int(input())

firstPart, secondPart = divmod(numbers, 1000);

firstSing, secondSing = divmod(firstPart, 10)

thirdNumber = secondPart // 100

fourthSing = (secondPart - (thirdNumber*100)) // 10
fifthSing = (secondPart - (thirdNumber*100)) % 10

result = (fifthSing * 10000) + (fourthSing * 1000) + (thirdNumber * 100) + (secondSing * 10) + firstSing

print(result)