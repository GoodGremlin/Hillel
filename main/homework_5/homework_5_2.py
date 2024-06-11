operators = '+-*/'

isContinue = True

while isContinue:
    expression = input('Enter a example: ')
    result = ''
    operator = ''

    for char in expression:
        if char in operators:
            operator = char
            break

    if operator:
        number1, number2 = map(int, expression.split(operator))

        if operator == '+':
            result = number1 + number2
        elif operator == '-':
            result = number1 - number2
        elif operator == '*':
            result = number1 * number2
        elif operator == '/':
            if number2 != 0:
                result = number1 / number2
            else:
                result = 'Error: Division by zero'
        else:
            result = 'Error: Invalid operator'

        print(result)

        answerToContinue = input('Continue? [y/n]: ')

        isContinue = answerToContinue.lower() == 'y'
