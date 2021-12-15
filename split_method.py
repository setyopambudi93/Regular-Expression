import re

# separate
sentence = 'In 2020, the whole world is hit by a pandemic. Until the end of 2021 there is still no improvement'
pattern = r'\s' # space
result = re.split(pattern, sentence)
print(result)
