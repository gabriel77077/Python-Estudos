# Ler 2 números inteiros do teclado. Se o segundo for diferente de zero, calcular e imprimir
# o quociente do primeiro pelo segundo. Caso contrário, imprimir a mensagem: “DIVISÃO
# POR ZERO”.
numero1 = int(input("Digite um número insteiro: "))
numero2 = int(input("Digite outro número inteiro: "))

if numero2 != 0 :
    print(numero1 / numero2)
else:
    print("Divisão por zero")
