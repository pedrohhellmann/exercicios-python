preço = float(input("Digite o preço do produto: "))
quantidade_comprada = int(input("Digite a quantidade comprada: "))
total = preço * quantidade_comprada
print(f"o total a pagar é: R${total:.2f}")