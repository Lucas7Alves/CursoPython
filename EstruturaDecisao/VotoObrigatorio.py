# Escreva um programa para receber a idade de uma pessoa.
# Informar quando a pessoa é obrigado a votar.
# Informar quando o voto for opcional (16, 17 e acima de 69 anos).

idade = int(input("Digite sua idade: "))

if idade > 17 and idade < 70:
    print("Voto obrigatório!!")
elif idade >= 16 or idade >= 70:
    print("Voto opcional!")
else:
    print("Não pode votar")