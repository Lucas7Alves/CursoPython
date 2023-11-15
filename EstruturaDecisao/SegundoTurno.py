# Sabendo-se  que para eleição de presidente estão concorrendo 3 candidatos,
# elabore um programa que, a partir dos votos obtidos no primeiro turno,
# informe se haverá ou não o segundo turno da eleição.

# Observações:
# Para  haver segundo turno os votos de um dos candidatos
# não deve ultrapassar a soma de votos dos demais candidato.
# Considerar que não houve empate.

#Testa se haverá ou não segundo turno
def segundoTurno (votoCandidato1, votoCandidato2, votoCandidato3):
    if votoCandidato3 > (votoCandidato1 + votoCandidato2) or votoCandidato2 > (votoCandidato1 + votoCandidato3) or votoCandidato1 > (votoCandidato3 + votoCandidato2):
        return "Não haverá segundo turno!"
    else:
        return "Haverá segundo turno!"

votoCandidato1 = int(input("Quantos votos teve o primeiro candidato?"))
votoCandidato2 = int(input("Quantos votos teve o segundo candidato?"))
votoCandidato3 = int(input("Quantos votos teve o terceiro candidato?"))




print(segundoTurno(votoCandidato1,votoCandidato2, votoCandidato3))