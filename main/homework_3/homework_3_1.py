firstSing = int(input('Enter the first number: '))
action = input('Enter the action: ')
secondSing = int(input('Enter the second number: '))
result = ''

if action == '+':
    result = firstSing + secondSing
elif action == '-':
    result = firstSing - secondSing
elif action == '*':
    result = firstSing * secondSing
elif action == '/' and (secondSing > 0 and firstSing > 0):
    result = firstSing / secondSing


print(result);