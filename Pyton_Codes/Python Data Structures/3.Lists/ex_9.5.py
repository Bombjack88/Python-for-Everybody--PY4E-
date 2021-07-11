file_name=input('Nome do ficheiro:')
if len(file_name)<1:
    file=open('mbox-short.txt')
else:
    file=open(file_name)

domain_name=dict()
for linha in file:
    linha=linha.rstrip()
    if linha.startswith('From'):
        palavras=linha.split()
        if len(palavras)>=3:
            dominio=palavras[1][palavras[1].find('@')+1:]
            #print(dominio)
            domain_name[dominio]=domain_name.get(dominio,0)+1
print(domain_name)