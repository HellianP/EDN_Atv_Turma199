hash=("_" * 20)
#1- Área da circunferência

print(hash,"Área da Circunferência".center(20),hash)
pi=3.14159265
raio = float(input("Digite o valor do raio: "))
area = pi*(raio**2)
print("A={:.4f}".format(area))

#2- Classificador de Idade
print(hash,"Classificador de Idade".center(20),hash)
idade = int(input("Digite sua idade: "))
print("Criança" if idade <= 12 else "Adolescente" if idade <= 17 else "Adulto" if idade <= 59 else "Idoso")
#3- Calculadora de IMC

print(hash,"Calculadora de IMC".center(20),hash)
peso = float(input("Digite seu peso em kilos , Exemplo 70: "))
altura = float(input("Digite sua altura em metros , Exemplo 1.70: "))
imc = peso / (altura ** 2)
print("abaixo do peso" if imc < 18.5 else "peso normal" if imc < 25 else "sobrepeso" if imc < 30 else "obeso")

#4- Conversor de Temperatura 

print(hash,"Conversor de Temperatura".center(20),hash)
temp = float(input("Digite a temperatura a ser convertida: "))
unidade_origem = input("Digite a unidade de origem (C, F, K): ").upper()
unidade_destino = input("Digite a unidade de destino (C, F, K): ").upper()
if unidade_origem == "C":
    if unidade_destino == "F":
        temp_convertida = (temp * 9/5) + 32
    elif unidade_destino == "K":
        temp_convertida = temp + 273.15
    else:
        temp_convertida = temp
elif unidade_origem == "F":
    if unidade_destino == "C":
        temp_convertida = (temp - 32) * 5/9
    elif unidade_destino == "K":
        temp_convertida = (temp - 32) * 5/9 + 273.15
    else:
        temp_convertida = temp
elif unidade_origem == "K":
    if unidade_destino == "C":
        temp_convertida = temp - 273.15
    elif unidade_destino == "F":
        temp_convertida = (temp - 273.15) * 9/5 + 32
    else:
        temp_convertida = temp

print("Temperatura convertida: {:.2f} {}".format(temp_convertida, unidade_destino))


#5- Verificador de Ano Bissexto
print(hash,"Verificador de Ano Bissexto".center(20),hash)
ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")

#6- Calculadora de Comissão
print(hash,"Calculadora de Comissão".center(20),hash)
nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo do vendedor: "))
total_vendas = float(input("Digite o valor total das vendas efetuadas no mês: "))
comissao = total_vendas * 0.15
total_receber = salario_fixo + comissao
print("TOTAL A RECEBER: R$ {:.2f}".format(total_receber))

7#- Calculadora da Média
print(hash,"Calculadora da Média".center(20),hash)
n1, n2, n3, n4 = map(float, input("Digite as quatro notas separadas por espaço: ").split())
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10
print("Media: {:.1f}".format(media))
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input("Digite a nota do exame: "))
    print("Nota do exame: {:.1f}".format(nota_exame))
    media_final = (media + nota_exame) / 2
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(media_final))
