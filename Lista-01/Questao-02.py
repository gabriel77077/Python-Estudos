#Calcular a média final (usando a ponderação da UFRN) dadas as notas das 3 provas e
#produzir uma saída com a média e a situação do aluno de acordo com o seguinte critério:
#média >= 7, aprovado; 5 < média < 7, recuperação; média < 5, reprovado.

nota_01 = input("Digite nota 01: ")
nota_02 = input("Digite nota 02: ")
nota_03 = input("Digite nota 03: ")
nota_01 = int(nota_01)
nota_02 = int(nota_02)
nota_03 = int(nota_03)

media = (nota_01 + nota_02 + nota_03) / 3

if media >= 7 :
    print("Aprovado")
if media >= 5 and media < 7 :
    print("Recuperação")
if media < 5 :
    print("Reprovado")
