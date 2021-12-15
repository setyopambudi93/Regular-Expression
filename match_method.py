import re

# first stop
sentence = 'Today is Wednesday'
pattern = r'\w{5}' # alphanumeric
result = re.match(pattern, sentence)
print(result)
