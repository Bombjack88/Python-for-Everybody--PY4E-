# teste: regex_sum_42.txt; assigment:regex_sum_1282830.txt
# Obter todos os números de um texto e depois somar

import re
file_name=input('Enter the file name:')
if len(file_name)<1:
    file=open('regex_sum_42.txt')
else:
    file=open(file_name)
res=list()
for line in file:
    linha=re.findall('[0-9]+',line)
    if len(linha)>=1:
        for i in linha:
            res.append(float(i))
print(res)
print(len(res))
soma=0
for i in res:
    soma=soma+i
print(soma)
