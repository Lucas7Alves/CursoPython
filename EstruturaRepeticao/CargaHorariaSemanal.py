# Escreva um programa para receber o tipo de aula (P para presencial ou O para online) 
# das aulas dos 5 dias úteis de uma semana. 
# Criticar para só aceitar P ou O.

#Mostrar:
#- Carga horária semanal de aulas presenciais 
#- Carga horária semanal de aulas online
#- Carga horária semanal total
#Obs.:
#* Aulas presenciais tem carga horária de 3 horas
#* Aulas online tem carga horária de 1,5 horas

cargaHorariaSemanalP = 0.0
cargaHorariaSemanalO = 0.0
contador = 0
while(True):
    resposta = input("Informe seu tipo de aula [P] ou [O]")
    resposta = resposta.upper()
    if resposta[0] == 'P':
        cargaHorariaSemanalP += 3
        contador += 1
    elif resposta[0] == 'O':
        cargaHorariaSemanalO += 1.5
        contador += 1 
    else:
        print("Tipo de curso inválido!")

    if contador == 5:
        break

print("Carga horaria presencial: "+ str(cargaHorariaSemanalP))
print("Carga horaria online: "+str(cargaHorariaSemanalO))
print("Carga horaria total: "+str((cargaHorariaSemanalP + cargaHorariaSemanalO)))

