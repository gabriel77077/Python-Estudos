#Para ler 3 números reais do teclado e verificar se o primeiro é maior que a soma dos
#outros dois.

numero1 = input("Digite um número real: ")
numero2 = input("Digite um número real: ")
numero3 = input("Digite um número real: ")

numero1 = float(numero1)
numero2 = float(numero2)
numero3 = float(numero3)

if numero1 > (numero2 + numero3):
    print(numero1," é maior que ",(numero2+numero3))
else:
    print("não é maior")
