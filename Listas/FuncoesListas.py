# Funções em lista

frutas = ["Uva", "Pera", "Maçã", "Banana"]
verduras = ["Cebola", "Pimentão"]

frutas.extend(verduras) #Juntando 2 listas


frutas.append(12) #Adiciona um valor na ultima posição


frutas.insert(1, "Abacaxi") #Adiciona um valor onde for informado

frutas.remove(12) #Remove o valor desejado

frutas.pop() #Remove o ultimo valor 

print(frutas.index("Uva")) # retorna a posição do valor

#Conta quantos valores desse mesmo parâmetro foi encontrado
print(frutas.count("Abacaxi")) 

frutas.sort() #põe a lista em ordem alfabetica

frutas.reverse() #ordena de trás para frente a lista

print(frutas)
