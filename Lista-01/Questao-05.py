#Que informe a área e o volume de um cilindro.

raio = input("Digite o raio da base em metros: ")
altura = input("Digite a altura do cilindro em metros: ")

raio = float(raio)
altura = float(altura)

area = (raio * raio) * 3.14
volume = area * altura

print("Área da base: ",area)
print("Volume do cilindro: ",volume)
