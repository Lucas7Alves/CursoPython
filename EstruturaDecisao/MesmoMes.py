# Elabore um programa para ler o registro de um dia (número do dia anterior e número do dia atual) 
# e mostrar se os números dos dias informado determina ser do mesmo mês ou ser um novo mês.

registroDiaAnterior = int(input("Informe o dia anterior:"))
registroDiaAtual = int(input("Informe o dia atual:"))

if registroDiaAnterior > registroDiaAtual:
    print("Novo mês!!")
else:
    print("Mesmo mês!")

