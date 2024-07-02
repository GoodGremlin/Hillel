import re


def popular_words(text, words):
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    text_list = cleaned_text.split()

    count_dict = {}
    for word in text_list:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1

    result = {}
    for word in words:
        result[word] = count_dict.get(word, 0)

    return result

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')

