# Questão 16
n = int(input('Digite seu número: '))
n1 = n//100
n2 = (n//10)-(n1*10)
n3 = n-(n1*100)-(n2*10)

print(f'Seu número, quando invertido, se torna: {n3}{n2}{n1}')