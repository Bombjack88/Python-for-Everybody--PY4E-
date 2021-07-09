#the most commom words
file_name=input('Nome do ficheiro:')
if len(file_name)<1:
    file=open('romeo-full.txt')
else:
    file=open('file_name')
count=dict()
for line in file:
    line=line.rstrip().lower()
    palavras=line.split()
    #print(palavras)
    for palavra in palavras:
        count[palavra]=count.get(palavra,0)+1

#sort by values
lista=list()
for key, value in count.items():
        lista.append((value,key))
#print(sorted(lista,reverse=True))
lista.sort(reverse=True)
for value, key in lista[0:10]:
    print(key,value)
