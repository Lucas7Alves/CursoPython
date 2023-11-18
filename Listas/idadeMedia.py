# receber a idade de 5 pessoas. Mostre a média das 
# idades das pessoas da terceira idade.

# Obs: Terceira idade a partir de 60 anos.

idade = 0
terceiraIdade = []
contador = 0
for i in range(5):
    idade = int(input("Digite uma idade: "))

    if idade >= 60:
        contador = contador + 1
        terceiraIdade.append(idade)
acumulador = 0
for i in range(contador):
    acumulador = acumulador + terceiraIdade[i]

mediaIdade = acumulador/contador

print(mediaIdade)

