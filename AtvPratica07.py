import csv
import json
import statistics

hash = "_" * 20

# 1 - Leitura de Log e Cálculo de Estatísticas
def analisar_log(arquivo: str):
    # Lê um arquivo contendo tempos de execução de treinamento e calcula média e desvio padrão.
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            linhas = f.readlines()

        # Extrai apenas valores numéricos
        tempos = [float(l.strip()) for l in linhas if l.strip().replace('.', '', 1).isdigit()]

        if not tempos:
            raise ValueError("Nenhum dado numérico válido encontrado no arquivo.")

        media = statistics.mean(tempos)
        desvio = statistics.stdev(tempos) if len(tempos) > 1 else 0.0

        print(f"Média dos tempos: {media:.2f}")
        print(f"Desvio padrão: {desvio:.2f}")

    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o nome e o caminho do arquivo.")
    except ValueError as ve:
        print(f"Erro de valor: {ve}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


# 2 - Escrita de Arquivo CSV
def escrever_csv(arquivo: str):
    # Cria um arquivo CSV e grava informações pessoais (Nome, Idade e Cidade).
    try:
        with open(arquivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Nome", "Idade", "Cidade"])

            while True:
                nome = input("Digite o nome: ").strip()
                idade = input("Digite a idade: ").strip()
                cidade = input("Digite a cidade: ").strip()
                writer.writerow([nome, idade, cidade])

                continuar = input("Deseja adicionar outra pessoa? (s/n): ").strip().lower()
                if continuar != 's':
                    break

        print(f"Arquivo '{arquivo}' criado e salvo com sucesso.")

    except Exception as e:
        print(f"Erro ao escrever o arquivo CSV: {e}")


# 3 - Leitura de Arquivo CSV
def ler_csv(arquivo: str):
    # Lê e exibe os dados de um arquivo CSV contendo Nome, Idade e Cidade.
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            leitor = csv.reader(f)
            cabecalho = next(leitor, None)
            print(f"{' | '.join(cabecalho)}")
            print(hash * 3)
            for linha in leitor:
                print(f"{' | '.join(linha)}")
    except FileNotFoundError:
        print("Arquivo CSV não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")


# 4 - Leitura e Escrita de Arquivo JSON
def manipular_json(arquivo: str):
    # Cria ou lê um arquivo JSON contendo informações de uma pessoa.
    try:
        escolha = input("Deseja (1) criar/editar ou (2) ler o arquivo JSON? ").strip()
        if escolha == '1':
            nome = input("Digite o nome: ")
            idade = input("Digite a idade: ")
            cidade = input("Digite a cidade: ")

            pessoa = {
                "nome": nome,
                "idade": idade,
                "cidade": cidade
            }

            with open(arquivo, 'w', encoding='utf-8') as f:
                json.dump(pessoa, f, ensure_ascii=False, indent=4)

            print(f"Arquivo JSON '{arquivo}' criado/atualizado com sucesso.")

        elif escolha == '2':
            with open(arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                print("Dados do arquivo JSON:")
                for chave, valor in dados.items():
                    print(f"{chave.capitalize()}: {valor}")

        else:
            print("Opção inválida.")

    except FileNotFoundError:
        print("Arquivo JSON não encontrado.")
    except Exception as e:
        print(f"Erro ao manipular arquivo JSON: {e}")


# Função Principal
def main():
    print(hash, "Menu Principal".center(20), hash)
    print("Escolha uma das opções abaixo:")
    print("1 - Analisar Log de Treinamento")
    print("2 - Criar e Escrever Arquivo CSV")
    print("3 - Ler Arquivo CSV")
    print("4 - Ler e Escrever Arquivo JSON")

    try:
        opcao = int(input("Digite o número da opção desejada: "))
    except ValueError:
        print("Opção inválida! Por favor, digite um número de 1 a 4.")
        return

    if opcao == 1:
        print(hash, "Análise de Log".center(20), hash)
        arquivo = input("Digite o nome do arquivo de log (ex: log.txt): ")
        analisar_log(arquivo)

    elif opcao == 2:
        print(hash, "Escrita de Arquivo CSV".center(20), hash)
        arquivo = input("Digite o nome do arquivo CSV a ser criado (ex: dados.csv): ")
        escrever_csv(arquivo)

    elif opcao == 3:
        print(hash, "Leitura de Arquivo CSV".center(20), hash)
        arquivo = input("Digite o nome do arquivo CSV a ser lido: ")
        ler_csv(arquivo)

    elif opcao == 4:
        print(hash, "Manipulação de Arquivo JSON".center(20), hash)
        arquivo = input("Digite o nome do arquivo JSON (ex: pessoa.json): ")
        manipular_json(arquivo)

    else:
        print("Opção inválida! Escolha um número entre 1 e 4.")


if __name__ == "__main__":
    main()
