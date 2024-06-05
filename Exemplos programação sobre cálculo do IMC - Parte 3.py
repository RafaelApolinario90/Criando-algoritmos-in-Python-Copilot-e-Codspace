nome = 'Rafael Apolinário' # Str
idade = 34 # Int
altura = 1.80 # Float
e_maior = idade > 18 # Bool
peso = 86 # Float
# data_1 = True # Bool
# data_atual = 2022 # Int
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu Imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu Imc é {imc:.2f}')
print('{}  tem  {} anos de idade e seu Imc é {:.2f}'. format(nome, idade, imc))
print('{0}  tem  {1} anos de idade e seu Imc é {2}'. format(nome, idade, imc))
print('{n}  tem  {i} anos de e idade seu Imc é {im:2f}'. format(n=nome, i=idade, im=imc))
print('{n}  tem  {i} anos de e idade seu Imc é {im}'. format(n=nome, i=idade, im=imc))