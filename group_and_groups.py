import re

# only work for search and match method

sentence = 'The value of the composite stock price index fell on March 15.'
kalimat = 'Nilai Index Harga Saham Gabungan sempat jatuh pada 15 maret.'
pattern = r'.+\s(.+ex).+(\d{2}\s.+).'
result = re.search(pattern, kalimat)
hasil = result.groups()
print(hasil)
