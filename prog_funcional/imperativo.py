
# Abordagem Imperativa.
# Na imperativa se diz como algo deve ser feito, se dá o passo a passo.
# Exemplo, SQL é declarativo, se pede algo, sem dizer como deve ser feito, que é o oposto de Imperativo.

from calendar import mdays, month_name

# Lista todos os meses do ano com 31 dias com uma Abordagem Imperativa.

print('Meses com 31 dias:')
for mes in range(1, 13):
    if mdays[mes] == 31:
        print(f'- {month_name[mes]}')