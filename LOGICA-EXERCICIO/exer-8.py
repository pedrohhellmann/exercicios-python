idade = int(input("Digite a sua idade: "))

if idade < 0:
    print("Idade inválida.")
elif idade <= 12:
    print("Classificação: Criança")
elif idade <= 17:
    print("Classificação: Adolescente")
else:
    print("Classificação: Adulto")