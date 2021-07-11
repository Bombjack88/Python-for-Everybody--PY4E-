lista=list()
while True:
    num=input('Enter a number:')
    if num=='done':
        break
    else:
        num=float(num)
        lista.append(num)
print(f'Máximo {max(lista)}, Mínimo {min(lista)}')
