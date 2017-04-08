#Que gere o preço de um carro ao consumidor e os valores pagos pelo imposto e pelo lucro
#do distribuidor, sabendo o custo de fábrica do carro e que são pagos:
#a) de imposto: 45% sobre o custo do carro;
#b) de lucro do distribuidor: 12% sobre o custo do carro.

fabrica = input("Custo de fábrica: ")

fabrica = float(fabrica)

imposto = fabrica + (fabrica * 0.45)
distribuidor = imposto + (fabrica * 0.12)

print("Imposto: R$",imposto)
print("Preço de distribuidor: R$",distribuidor)
