# Questão 20
p = float(input('Insira o capital inical do juros compostos: '))
i = float(input('Insira a taxa de juros mensal em porcentagem: '))
t = float(input('Insira o tempo, em meses, do juros compostos: '))
m =  p * (1 + i/100)**t

print(f'O montante de seus juros compostos é: {m}R$.')