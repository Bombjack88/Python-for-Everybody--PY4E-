#sort lists
# file name: romeo.txt
filename=input('Enter the file name:')
file=open(filename)
lista=list()
final=list()
for line in file:
    lista=line.split()
    for i in lista:
        if i not in final:
            final.append(i)
final.sort()
print(final)


