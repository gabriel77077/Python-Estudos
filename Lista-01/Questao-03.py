#Calcular a quantidade dinheiro gasta por um fumante. Dados: o número de anos que ele
#fuma, o nº de cigarros fumados por dia e o preço de uma carteira.

anos = input("Anos como fumante: ")
cigarro = input("Cigarros por dia: ")
preco = input("Preço da unidade da carteira: ")

anos = int(anos)
cigarro = int(cigarro)
preco = float(preco)

total = (anos * 365) * (cigarro / 12) * preco

print("Total gasto:",total)
