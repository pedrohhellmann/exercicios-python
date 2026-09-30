positivo = 0

while True:
    num = int(input("Digite um número (ou 0 para sair): "))
    if num == 0:
        break
    elif num > 0:
        positivo += 1
    print(f"Quantidade de números positivos digitados: {positivo}")