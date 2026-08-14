# Questão 11
salario = int(input('Insira o seu salário:'))
inss = (salario*8/100)
I_Renda = (salario*5)/100
salario_liquido = salario-(inss+I_Renda)

print(f'O seu salário líquido é {salario_liquido}R$, em que foi descontado: {inss}R$, e {I_Renda}R$, dos impostos do INSS e Imposto de Renda, respectivamente.')