# Questão 14
tempo = int(input('Digite o tempo, em segundos, que você deseja converter: '))
minutos = tempo//60
seg_rest = tempo%60
horas = minutos//60
min_rest = minutos-(horas*60)

print(f'{tempo} segundos equivalem a: {horas}h {min_rest}min e {seg_rest}segundos.')