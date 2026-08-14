# Questão 1 
n1 = int(input("Insira seu primeiro número:"))
n2 = int(input("Insira seu segundo número:"))
soma = n1+n2
mult = n1*n2

print(f'A soma entre seus números é: {soma}')
print(f'O produto de seus números é: {mult}')

# Questão 2
n1 = int(input("Insira sua primeira nota:"))
n2 = int(input("Insira sua segunda nota:"))
n3 = int(input("Insira sua terceira nota:"))
media = (n1+n2+n3)/3
print(f'Sua média é: {media}')

# Questão 3
n = int(input("Insira um número:"))
sucessor = n+1
antecessor = n-1
print(f'O sucessor do seu número é: {sucessor}')
print(f'O antecessor do seu número é: {antecessor}')

# Questão 4
temp = int(input("Insira a temperatura em Celsius:"))
tempF = (temp*1.8)

print(f'Sua temperatura em Fahrenheit é: {tempF}')

# Questão 5
base = int(input("Insira a base do retângulo:"))
altura = int(input("Insira a altura do retângulo:"))
área = base*altura
perimetro = 2*(base+altura)

print(f'A área deste retângulo é {área}, e seu perímetro é {perimetro}')

# Questão 6
n = int(input('Insira seu número:'))
quadrado = n**2
raiz = n**0.5

print(f'O quadrado de seu número é {quadrado}, e sua raiz é {raiz}')

# Questão 7
preço = int(input("Insira o preço do produto:"))
porcentagem = int(input("Insira o desconto em porcentagem do produto:")) # Não colocar o símbolo "%" na porcentagem de desconto!
desconto = ((preço*porcentagem)/100)
custo = preço-desconto

print(f'O desconto de {porcentagem}% desse produto equivale à {desconto}R$, e seu custo ficou {custo}')

# Questão 8

reais = int(input('Insira o valor em reais:'))
dólar = reais/5.11  # Se desejar um valor menos quebrado, substitua o 5.11 por 5!

print(f'{reais}R$ em dólar são: {dólar}$')

# Questão 9
n1 = int(input("Insira sua primeira nota:"))
n2 = int(input("Insira sua segunda nota:"))
n3 = int(input("Insira sua terceira nota:"))
media_pond = ((n1*2)+(n2*3)+(n3*5))/10

print(f'A média ponderada, de pesos 2, 3 e 5, respectivamente, de suas notas é: {media_pond}')

# Questão 10
pessoas = int(input('Insira a quantia de pessoas:'))
valor = int(input('Insira o valor da conta:'))
valor_total = valor+(valor/10)
por_pessoa = valor_total/pessoas

print(f'O valor total da conta, com 10% de taxa de serviço, ficou {valor_total}R$. Dividindo esse valor pra {pessoas} pessoas, cada um deve pagar: {por_pessoa}.')

# Questão 11
salario = int(input('Insira o seu salário:'))
inss = (salario*8/100)
I_Renda = (salario*5)/100
salario_liquido = salario-(inss+I_Renda)

print(f'O seu salário líquido é {salario_liquido}R$, em que foi descontado: {inss}R$, e {I_Renda}R$, dos impostos do INSS e Imposto de Renda, respectivamente.')

# Questão 12
velocidade = int(input('Insira a velocidade do veículo em Km/h (Quilômetros por hora):'))
tempo = int(input('Insira o tempo, em horas, que você dirigiu o veículo:'))
tanque_i = int(input('Insira a quantia de gasolina, em litros, no tanque quando o trajeto foi iniciado:'))
tanque_f = int(input('Insira a quantia de gasolina, em litros, no tanque quando o trajeto foi finalizado:'))
l_gastos = tanque_i-tanque_f
distância = velocidade*tempo
kml = distância/l_gastos

print(f'O consumo médio de gasolina do veículo em Quilômetro(s) por Litro foi: {kml} Km/l')

# Questão 13
r = float(input('Insira o raio do círculo [OBS: O resultado estará na mesma unidade de medida do raio!] :'))
area = (r**2)*3.14159 
peri = r*2*3.14159

print(f'A área do circulo de raio {r} é {area}, e seu perímetro é {peri}.')

# Questão 14
tempo = int(input('Digite o tempo, em segundos, que você deseja converter: '))
minutos = tempo//60
seg_rest = tempo%60
horas = minutos//60
min_rest = minutos-(horas*60)

print(f'{tempo} segundos equivalem a: {horas}h {min_rest}min e {seg_rest}segundos.')

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

# Questão 16
n = int(input('Digite seu número: '))
n1 = n//100
n2 = (n//10)-(n1*10)
n3 = n-(n1*100)-(n2*10)

print(f'Seu número, quando invertido, se torna: {n3}{n2}{n1}')

# Questão 17
i = int(input('Digite sua idade: '))
m = i*12
d = i*365

print(f'Se você têm {i} anos, você viveu: {m} meses e {d} dias.')

# Questão 18
c1 = float(input('Insira o valor do 1o cateto do seu triângulo retangulo: '))
c2 = float(input('Insira o valor do 2o cateto do seu triângulo retangulo: '))
h = (c1**2+c2**2)**0.5


print(f'O valor da hipotenusa do seu triângulo é: {h}.')

# Questão 19
b = float(input('Insira a largura da parede: '))
h = float(input('Insira a altura da parede: '))
parede = b*h
tinta = parede/2

print(f'A quantidade de tinta, em litros, para pintar a parede será de: {tinta}l.')

# Questão 20
p = float(input('Insira o capital inical do juros compostos: '))
i = float(input('Insira a taxa de juros mensal em porcentagem: '))
t = float(input('Insira o tempo, em meses, do juros compostos: '))
m =  p * (1 + i/100)**t

print(f'O montante de seus juros compostos é: {m}R$.')