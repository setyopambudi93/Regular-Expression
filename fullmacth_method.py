import re

# Whole, except new line

sentence = 'This is right'
pattern = r'.{13}' # all
result = re.fullmatch(pattern, sentence)
print(result)
