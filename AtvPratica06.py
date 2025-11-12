import random
import string
import requests

hash = "_" * 20
# 1 - Gerador de Senha Aleatória
def gerar_senha(tamanho: int) -> str:
    # Gera uma senha aleatória contendo letras, números e caracteres especiais.
    if tamanho <= 0:
        raise ValueError("O tamanho da senha deve ser maior que zero.")
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


# 2 - Gerador de Perfil de Usuário Aleatório
def gerar_usuario_aleatorio():
    # Gera um perfil de usuário aleatório a partir da API Random User Generator.
    url = "https://randomuser.me/api/"
    resp = requests.get(url)
    resp.raise_for_status()
    dados = resp.json()
    usuario = dados["results"][0]
    nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario["email"]
    pais = usuario["location"]["country"]
    print(f"Nome: {nome_completo}")
    print(f"Email: {email}")
    print(f"País: {pais}")


# 3 - Consulta de Endereço via CEP
def consultar_endereco(cep: str):
    # Consulta o endereço correspondente a um CEP no Brasil usando a API ViaCEP.
    cep_limpo = cep.strip().replace('-', '').replace('.', '')
    if not (cep_limpo.isdigit() and len(cep_limpo) == 8):
        raise ValueError("CEP inválido. Informe 8 dígitos sem formatação.")
    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
    resp = requests.get(url)
    resp.raise_for_status()
    dados = resp.json()
    if "erro" in dados:
        raise ValueError("CEP não encontrado.")
    print(f"Logradouro: {dados.get('logradouro')}")
    print(f"Bairro: {dados.get('bairro')}")
    print(f"Cidade: {dados.get('localidade')}")
    print(f"Estado: {dados.get('uf')}")


# 4 - Consulta de Cotação de Moeda 
def consultar_cotacao(moeda: str):
    # Consulta a cotação da moeda informada em relação ao Real Brasileiro (BRL).
    moeda = moeda.upper().strip()
    par = f"{moeda}-BRL"
    url = f"https://economia.awesomeapi.com.br/json/last/{par}"
    resp = requests.get(url)
    resp.raise_for_status()
    dados = resp.json()
    key = f"{moeda}BRL"
    if key not in dados:
        raise ValueError("Par de moeda não encontrado.")
    info = dados[key]
    print(f"Moeda: {info.get('name')}")
    print(f"Valor atual (bid): {info.get('bid')}")
    print(f"Máximo (high): {info.get('high')}")
    print(f"Mínimo (low): {info.get('low')}")
    print(f"Data/hora da última atualização: {info.get('create_date')}")


def main():
    print(hash, "Menu Principal".center(20), hash)
    print("Escolha uma das opções abaixo:")
    print("1 - Gerar Senha Aleatória")
    print("2 - Gerar Perfil de Usuário Aleatório")
    print("3 - Consultar Endereço por CEP")
    print("4 - Consultar Cotação de Moeda")

    try:
        opcao = int(input("Digite o número da opção desejada: "))
    except ValueError:
        print("Opção inválida! Por favor, digite um número de 1 a 4.")
        return
   
    if opcao == 1:
        print(hash, "Gerador de Senha Aleatória".center(20), hash)
        try:
            tamanho = int(input("Digite o tamanho desejado da senha: "))
            senha = gerar_senha(tamanho)
            print(f"Senha gerada: {senha}")
        except ValueError as ve:
            print(f"Erro de valor: {ve}")

    elif opcao == 2:
        print(hash, "Gerador de Usuário Aleatório".center(20), hash)
        try:
            gerar_usuario_aleatorio()
        except Exception as e:
            print(f"Erro ao gerar perfil: {e}")

    elif opcao == 3:
        print(hash, "Consulta de Endereço por CEP".center(20), hash)
        try:
            cep = input("Digite o CEP (8 dígitos): ")
            consultar_endereco(cep)
        except ValueError as ve:
            print(f"Erro de valor: {ve}")
        except Exception as e:
            print(f"Erro ao consultar CEP: {e}")

   
    elif opcao == 4:
        print(hash, "Consulta de Cotação de Moeda".center(20), hash)
        try:
            moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ")
            consultar_cotacao(moeda)
        except ValueError as ve:
            print(f"Erro de valor: {ve}")
        except Exception as e:
            print(f"Erro ao consultar cotação: {e}")

    else:
        print("Opção inválida! Escolha um número entre 1 e 8.")


if __name__ == "__main__":
    main()
