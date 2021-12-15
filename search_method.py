import re

# whole , first , stop
my_text = 'Indonesia managed to get out of colonialism in 1945'
pattern = r'\d{4}' # digit
result = re.search(pattern, my_text) # formula
print(result)
