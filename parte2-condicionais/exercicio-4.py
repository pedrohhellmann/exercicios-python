nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
nota4 = int(input("Digite a quarta nota: "))


media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 6:
    print(f"A média do aluno é {media:.2f}. Aprovado!")
elif media >= 4 and media <= 5.9:
    print(f"A média do aluno é {media:.2f}. Recuperação!")
else:
    print(f"A média do aluno é {media:.2f}. Reprovado!")