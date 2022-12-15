 #! python

import csv

# Desta maneira ele já entende que é um arquivo .csv
# Simplifica todo o processo.

with open('pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('Nome: {}, Idade: {}'.format(*pessoa))