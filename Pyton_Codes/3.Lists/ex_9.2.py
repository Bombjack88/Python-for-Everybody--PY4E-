file=input('Enter the file name:')
if len(file)<1:
    file=open('mbox-short.txt')
else:
    file=open('file')
conta={}
for line in file:
    line=line.rstrip()
    if line.startswith('From'):
        palavras=line.split()
        if len(palavras)>=3:
            dia_semana=palavras[2]
            #print(dia_semana)
            conta[dia_semana]=conta.get(dia_semana,0)+1
print(conta)
