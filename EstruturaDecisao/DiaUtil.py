# Elabore  um programa para ler o número do dia da semana
# (1-domingo; 2-segunda, ..., 7 - sábado) e
# informar se é um dia útil ou final de semana.

print("1 - Domingo, 2 - Segunda, 3 - Terça, 4 - Quarta, "
      "5 - Quinta, 6 - Sexta, 7 - Sábado")
diaSemana = int(input("Digite o número do dia da semana da semana: "))

if diaSemana == 7 or diaSemana == 1:
    print("Final de semana!")
elif diaSemana > 7 or diaSemana < 1:
    print("Dia inválido!")
else:
    print("Dia útil!")

