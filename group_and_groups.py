import re

# only work for search and match method

sentence = 'The value of the composite stock price Index fell on March 15.'
sentences = 'Nilai Index Harga Saham Gabungan sempat jatuh pada 15 maret.'
pattern = r'.+\s(.+ex)' \
          r'.+(\d{2}\s.+).'
pattern1 = r'.+\s(.+ex)' \
           r'.+\s(.+ch\s\d{2})'
result = re.search(pattern1, sentence)
hasil = result.groups()
print(hasil)

