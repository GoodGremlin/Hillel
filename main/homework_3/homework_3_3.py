import math

firstList = [1, 2, 3, 4, 5]
secondList = [1, 2, 4, 5]
emptyList = []

mainList = secondList

mainListLength = len(mainList)
mainListMiddleIndex = math.ceil(mainListLength / 2)

leftPart = mainList[0: mainListMiddleIndex]
rightPart = mainList[mainListMiddleIndex: mainListLength]

resultArray = [leftPart, rightPart]

print(resultArray)
