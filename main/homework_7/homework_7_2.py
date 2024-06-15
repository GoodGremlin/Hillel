def correct_sentence(text):
    first_sing = text[0]
    second_sing = text[len(text) - 1]

    if not first_sing.istitle():
        text = text.capitalize()

    if not second_sing == '.':
        text = text + '.'

    return text

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
