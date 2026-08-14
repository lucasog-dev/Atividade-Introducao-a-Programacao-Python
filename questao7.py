# Questão 7
preço = float(input("Insira o preço do produto:"))
porcentagem = int(input("Insira o desconto em porcentagem do produto:")) # Não colocar o símbolo "%" na porcentagem de desconto!
desconto = ((preço*porcentagem)/100)
custo = preço-desconto

print(f'O desconto de {porcentagem}% desse produto equivale à {desconto}R$, e seu custo ficou {custo}')