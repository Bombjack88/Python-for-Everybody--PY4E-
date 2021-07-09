file=input('Nome do ficheiro:')
if len(file)<1:
    file=open('mbox-short.txt')
else:
    file=open(file)
dict={}
for linha in file:
    linha=linha.rstrip()
    if linha.startswith('From'):
        words=linha.split()
        #print(words)
        if len(words)>3:
            dict[words[1]]=dict.get(words[1],0)+1
print(dict)