import random

mainList = [random.randint(0, 3) for item in range(7)]
result = 0

print(mainList)

for index in range(len(mainList)):
    if index % 2 == 0:
        result += mainList[index]
    elif index == len(mainList) - 1:
        result *= mainList[index]


print(result)