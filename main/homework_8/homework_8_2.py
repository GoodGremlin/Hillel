import re

def is_palindrome(text):
    text = re.sub(r'[^\w\u2026]', '', text).lower()
    return [text[i] for i in range(len(text) // 2)] == [text[len(text) - 1 - i] for i in range(len(text) // 2)]



assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
