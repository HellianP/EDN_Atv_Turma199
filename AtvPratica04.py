hash=("_" * 20)
#Calculadora Pytnon
print(hash,"Calculadora Python".center(20),hash)
while (1):
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação que desejas (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                raise ZeroDivisionError("Divisão por zero não é permitida.")
            resultado = num1 / num2
        else:
            raise ValueError("Operação inválida. Use +, -, *, ou /.")

        print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")
        break

    except ValueError as VE:
        print(f"Erro de valor: {VE}. Por favor, tente novamente.")
    except ZeroDivisionError as ZDE:
        print(f"Erro de divisão: {ZDE}. Por favor, tente novamente.")
    except Exception as Ex:
        print(f"Ocorreu um erro inesperado: {Ex}. Por favor, tente novamente.")

#Registro de notas
print(hash,"Registro de Notas".center(20),hash)

notas = []
while (1):
    entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim': 
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota) # Adiciona a nota à lista, isso se ela for se for válida né
        else:
            print("Nota inválida. Digite uma nota entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'fim'.")
if notas:
    media = sum(notas) / len(notas)
    print(f"A média das notas é: {media:.2f}")  
else:
    print("Nenhuma nota foi registrada.")

#Verificador de senha forte
print(hash,"Verificador de Senha Forte".center(20),hash)
while (1):
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")
    if senha.lower() == 'sair':
        print("Encerrando o verificador de senhas.")
        break
    if len(senha) < 8:
        print("Senha fraca: deve ter pelo menos 8 caracteres.")
        continue
    if not any(char.isdigit() for char in senha):
        print("Senha fraca: deve conter pelo menos um número.")
        continue
    if len(senha) >= 8 and any(char.isdigit() for char in senha):
        print("Senha forte!")   
    break
#Verificador de números pares e ímpares
print(hash,"Verificador de Números Pares e Ímpares".center(20),hash)
pares = 0
impares = 0
while (1):
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        break
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
            pares += 1
        else:
            print(f"O número {numero} é ímpar.")
            impares += 1
    except ValueError as VE:
        print(f"Erro de valor: {VE}. Por favor, digite um número inteiro ou 'fim'.")
print(f"Números pares digitados: {pares}")
print(f"Números ímpares digitados: {impares}")