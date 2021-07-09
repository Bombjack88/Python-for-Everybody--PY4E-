name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hist=dict()
for line in handle:
    if line.startswith('From:'):
        words=line.split()
        if words[1] not in hist:
            hist[words[1]]=1
        else:
            hist[words[1]]=hist[words[1]]+1
#print(hist)
nome=conta=None
for a,b in hist.items():
    if conta==None or b>conta:
        nome=a
        conta=b
print(nome,conta)


# Alternativa
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hist=dict()
for line in handle:
    if line.startswith('From:'):
        words=line.split()
        hist[words[1]]=hist.get(words[1],0)+1
#print(hist)
nome=conta=None
for a,b in hist.items():
    if conta==None or b>conta:
        nome=a
        conta=b
print(nome,conta)