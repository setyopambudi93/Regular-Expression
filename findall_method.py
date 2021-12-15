import re

# find all, scan from left to right

sentence = 'In 2020, the whole world is hit by a pandemic. Until the end of 2021 there is still no improvement'
pattern = r'\d{4}'
result = re.findall(pattern, sentence)
print(result)
