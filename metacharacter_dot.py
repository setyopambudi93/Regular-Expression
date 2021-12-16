import re
sentence = 'This is gonna will match all of content'
pattern = r'.+'  # Parentheses or not
result = re.search(pattern, sentence)
print(result)