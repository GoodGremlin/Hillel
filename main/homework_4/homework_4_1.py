import random

mainList = [random.randint(0, 5) for item in range(50)]
secondList = []

print(mainList)

for index in range(len(mainList) - 1, -1, -1):
    if mainList[index] == 0:
        mainList.append(mainList.pop(index))

print(mainList)