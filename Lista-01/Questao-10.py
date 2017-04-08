#Ler 2 números inteiros do teclado (A e B), verificar e imprimir qual deles é o maior, ou a
#mensagem “A=B” caso sejam iguais.

numeroA = input("Digite um valor inteiro para A: ")
numeroB = input("Digite um valor inteiro para B: ")

if numeroA > numeroB:
    print("A é maior")
if numeroB > numeroA:
    print("B é maior")
if numeroA == numeroB:
    print("A = B")
