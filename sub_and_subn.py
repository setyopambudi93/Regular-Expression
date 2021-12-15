import re

# replace
sentence = 'STOCK price movements of Indonesian shares can be seen globally through joint stock STOCK prices'
pattern = r'[A-Z]{2,}' # find capital
result = re.sub(pattern, 'INDEX', sentence) # formula without count
print(result)

# subn
sentence = 'STOCK price movements of Indonesian shares can be seen globally through joint stock STOCK prices'
pattern = r'[A-Z]{2,}' # find capital
result = re.subn(pattern, 'INDEX', sentence) # formula without count
print(result) # tuple

