file_name=input('Enter the file name:')
if len(file_name)<1:
    handle=open('mbox-short.txt')
else:
    handle=open(file_name)
horas=dict()
for line in handle:
    line=line.rstrip()
    if line.startswith('From'):
        words=line.split()
        if len (words)>3:
            #print(words[5])
            horas[words[5][:2]]=horas.get(words[5][:2],0)+1
#print(sorted(horas.items()))
lista=sorted(horas.items())
for a,b in lista:
    print(a,b)

