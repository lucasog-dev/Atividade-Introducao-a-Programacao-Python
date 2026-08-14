# Questão 12
velocidade = int(input('Insira a velocidade do veículo em Km/h (Quilômetros por hora):'))
tempo = int(input('Insira o tempo, em horas, que você dirigiu o veículo:'))
tanque_i = float(input('Insira a quantia de gasolina, em litros, no tanque quando o trajeto foi iniciado:'))
tanque_f = float(input('Insira a quantia de gasolina, em litros, no tanque quando o trajeto foi finalizado:'))
l_gastos = tanque_i-tanque_f
distância = velocidade*tempo
kml = distância/l_gastos

print(f'O consumo médio de gasolina do veículo em Quilômetro(s) por Litro foi: {kml} Km/l')