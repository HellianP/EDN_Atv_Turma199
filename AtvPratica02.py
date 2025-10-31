hash=("_" * 20)
#1- Conversor de Moeda 
print(hash,"Conversor de Moeda",hash)
valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60
valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro
print("Valor em dólares: $", round(valor_dolar, 2))
print("Valor em euros: €", round(valor_euro, 2))
#2- Calculadora de Desconto 
print(hash,"Calculadora de Desconto",hash)
nome_produto = "Camiseta"   
preco_original = 50.00
porcentagem_desconto = 20
valor_desconto = (porcentagem_desconto / 100) * preco_original
preco_final = preco_original - valor_desconto
print("Produto:", nome_produto)
print("Preço original: R$", preco_original)
print("Porcentagem de desconto:", porcentagem_desconto, "%")
print("Valor do desconto: R$", round(valor_desconto, 2))
print("Preço final: R$", round(preco_final, 2)) 
#3- Calculadora de Média Escolar 
print(hash,"Calculadora de Média Escolar",hash)
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5
media = (nota1 + nota2 + nota3) / 3
print("Notas:", nota1, ",", nota2, ",", nota3)
print("Média final: ", round(media, 2))
#4- Calculadora de Consumo de Combustível
print(hash,"Calculadora de Consumo de Combustível",hash)
distancia_percorrida = 300  # em km
combustivel_gasto = 25      # em litros
consumo_medio = distancia_percorrida / combustivel_gasto
print("Distância percorrida:", distancia_percorrida, "km")
print("Combustível gasto:", combustivel_gasto, "litros")
print("Consumo médio: ", round(consumo_medio, 2), "km/l")
#5- Calculadora de Soma com Entrada do Usuário
print(hash,"Calculadora de Soma com Entrada do Usuário".center(60),hash)
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
X = A + B
print("X =", X)
#6- Calculadora de salário por horas trabalhadas
print(hash,"Calculadora de Salário por Horas Trabalhadas".center(60),hash)
numero_funcionario = int(input("Digite o número do funcionário: "))
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor recebido por hora: "))
salario = horas_trabalhadas * valor_por_hora
print("Número do funcionário:", numero_funcionario)
print("SALÁRIO = R$ {:.2f}".format(salario))
