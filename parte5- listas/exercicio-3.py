minha_lista = [6, 7, 67, 607, 6767]

maior_valor = minha_lista[0]

for item in minha_lista:
    if item > maior_valor:
        maior_valor = item 

print(f"o maior valor da lista é: {maior_valor}")
