
valor = 0
while (True):
    
    try: 
        valor = float(input("Digite um valor: "))
    except ValueError as erro:
        print("Digite um número!!")

print(valor)

