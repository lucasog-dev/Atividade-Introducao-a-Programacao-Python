# Questão 15
dinheiro = int(input('Insira a quantia a quantia de dinheiro em reais:'))

if dinheiro >= 50:
    c50 = dinheiro//50 
    d20 = (dinheiro-(c50*50))//20 
    d10 = (dinheiro-(c50*50)-(d20*20))//10

else: 
    c50 = 1-1
    d20 = dinheiro//20 
    d10 = (dinheiro-(d20*20))//10

print(f'A quantidade de cédulas de 50, 20 e 10 reias, respectivamente é: {c50}, {d20} e {d10}.')
# OBS: Mesmo que a gente não tenha visto if e else ainda, pelo menos ate quarta (hoje), eu decidi usar pra ficar mais fácil, mas se quiser posso fazer normalmente.