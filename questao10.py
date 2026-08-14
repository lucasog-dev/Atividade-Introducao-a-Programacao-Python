# Questão 10
pessoas = int(input('Insira a quantia de pessoas:'))
valor = float(input('Insira o valor da conta:'))
valor_total = valor+(valor/10)
por_pessoa = valor_total/pessoas

print(f'O valor total da conta, com 10% de taxa de serviço, ficou {valor_total}R$. Dividindo esse valor pra {pessoas} pessoas, cada um deve pagar: {por_pessoa}.')
