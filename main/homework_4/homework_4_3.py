import random

mainList = [random.randint(0, 10) for item in range(random.randint(3, 10))]
newList = [mainList[i] for i in (0, 2, len(mainList) - 2)]

print(mainList)
print(newList)