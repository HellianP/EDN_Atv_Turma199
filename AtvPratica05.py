hash = "_" * 20

# 1️ Calculadora de Gorjeta
def calcular_gorjeta(conta: float, porcentagem: float) -> float:
    """Calcula a gorjeta com base no valor da conta e na porcentagem fornecida."""
    if conta < 0:
        raise ValueError("O valor da conta não pode ser negativo.")
    if porcentagem < 0:
        raise ValueError("A porcentagem da gorjeta não pode ser negativa.")
    gorjeta = conta * (porcentagem / 100)
    return gorjeta


# 2 Verificador de Palíndromo
def eh_palindromo(texto: str) -> str:
    """Verifica se uma palavra ou frase é um palíndromo."""
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())
    return "Sim" if texto_limpo == texto_limpo[::-1] else "Não"


# 3️ Calculadora de Desconto
def calcular_desconto(preco: float, desconto: float) -> float:
    """Calcula o preço final de um produto após aplicar o desconto."""
    if preco < 0:
        raise ValueError("O preço do produto não pode ser negativo.")
    if desconto < 0:
        raise ValueError("O percentual de desconto não pode ser negativo.")
    valor_desconto = preco * (desconto / 100)
    preco_final = preco - valor_desconto
    return preco_final


# 4️ Calculadora de Idade em Dias
def calcular_idade_em_dias(ano_nascimento: int, ano_atual: int = 2025) -> int:
    """Calcula a idade em dias com base no ano de nascimento."""
    if ano_nascimento > ano_atual:
        raise ValueError("O ano de nascimento não pode ser maior que o ano atual.")
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias

def main():
    print(hash, "Menu Principal".center(20), hash)
    print("Escolha uma das opções abaixo:")
    print("1 - Calcular Gorjeta")
    print("2 - Verificar Palíndromo")
    print("3 - Calcular Desconto")
    print("4 - Calcular Idade em Dias")

    try:
        opcao = int(input("Digite o número da opção desejada: "))
    except ValueError:
        print("Opção inválida! Por favor, digite um número de 1 a 4.")
        return

    # === Opção 1 ===
    if opcao == 1:
        print(hash, "Calculadora de Gorjeta".center(20), hash)
        try:
            conta = float(input("Digite o valor da conta: R$ "))
            porcentagem = float(input("Digite a porcentagem da gorjeta (ex: 15 para 15%): "))
            gorjeta = calcular_gorjeta(conta, porcentagem)
            total = conta + gorjeta
            print(f"A gorjeta de {porcentagem:.1f}% sobre R$ {conta:.2f} é R$ {gorjeta:.2f}.")
            print(f"O total a pagar é R$ {total:.2f}.")
        except ValueError as ve:
            print(f"Erro de valor: {ve}")

    elif opcao == 2:
        print(hash, "Verificador de Palíndromo".center(20), hash)
        frase = input("Digite uma palavra ou frase: ")
        resultado = eh_palindromo(frase)
        print(f"É palíndromo? {resultado}")

    elif opcao == 3:
        print(hash, "Calculadora de Desconto".center(20), hash)
        try:
            preco = float(input("Digite o preço do produto: R$ "))
            desconto = float(input("Digite o percentual de desconto (ex: 10 para 10%): "))
            preco_final = calcular_desconto(preco, desconto)
            print(f"O preço final após {desconto:.1f}% de desconto é R$ {preco_final:.2f}.")
        except ValueError as ve:
            print(f"Erro de valor: {ve}")

    elif opcao == 4:
        print(hash, "Calculadora de Idade em Dias".center(20), hash)
        try:
            ano_nascimento = int(input("Digite o ano de nascimento: "))
            idade_dias = calcular_idade_em_dias(ano_nascimento)
            print(f"Você tem aproximadamente {idade_dias} dias de vida.")
        except ValueError as ve:
            print(f"Erro de valor: {ve}")

    else:
        print("Opção inválida! Escolha um número entre 1 e 4.")


if __name__ == "__main__":
    main()
