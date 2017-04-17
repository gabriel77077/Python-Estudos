#Leia a velocidade máxima permitida em uma avenida e a velocidade com que o motorista
#estava dirigindo nela e calcule a multa que uma pessoa vai receber, sabendo que são
#pagos: a) 50 reais se o motorista estiver ultrapassar em até 10km/h a velocidade permitida
#(ex.: velocidade máxima: 50km/h; motorista a 60km/h ou a 56km/h); b) 100 reais, se o
#motorista ultrapassar de 11 a 30 km/h a velocidade permitida. c) 200 reais, se estiver
#acima de 31km/h da velocidade permitida.

maxima = input("Digite velocidade máxima permitida(KM/h): ")
motorista = input("Digite velocidade do motorista(KM/h):")

maxima = int(maxima)
motorista = int(motorista)

diferenca = motorista - maxima

if diferenca > 0 and diferenca <= 10:
    print("Multa: R$ 50,00")
elif diferenca > 10 and diferenca <= 30:
    print("Multa: R$ 100,00")
else diferenca > 30:
    print("multa: R$ 200,00")
