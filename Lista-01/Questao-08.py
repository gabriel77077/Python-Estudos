#Leia o número de termos de uma PA (Progressão Aritmética) e o seu primeiro e último termos e
#informe a soma dos elementos dessa PA.

numeros = input("Quantos números tem a PA: ")
primeiro = input("Primeiro número da PA: ")
ultimo = input("Ultimo número da PA: ")

numeros = int(numeros)
primeiro = int(primeiro)
ultimo = int(ultimo)

soma = (numeros * (primeiro + ultimo)) / 2

print("Soma dos elementos da PA: ", soma)
