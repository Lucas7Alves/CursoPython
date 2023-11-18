# Elabore um programa que recebe um número, se esse número for par
# eleve ao quadrado e coloque ele em uma lista, mostre a lista no final.

listaValores = []
valor = 0
while (True):

    valor = float(input("Digite um valor: "))

    if valor % 2 == 0 and valor != 0:
        valor = valor * valor
        listaValores.append(valor)
     
    decisao = input(("Deseja continuar? [s] [n]: "))
    if decisao == "n":
        break


print(listaValores)