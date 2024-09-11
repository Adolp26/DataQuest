import json

def palavra_existe_no_json(caminho_arquivo_json, palavra):
    try:
        with open(caminho_arquivo_json, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            
            dados_str = json.dumps(dados)
            if palavra in dados_str:
                return True
            else:
                return False
    except FileNotFoundError:
        print(f"Arquivo {caminho_arquivo_json} não encontrado.")
        return False
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON.")
        return False

caminho_arquivo = input("Digite o caminho do arquivo JSON: ")
palavra_buscar = input("Digite a palavra que deseja buscar no arquivo JSON: ")

if palavra_existe_no_json(caminho_arquivo, palavra_buscar):
    print(f"A palavra '{palavra_buscar}' foi encontrada no arquivo JSON.")
else:
    print(f"A palavra '{palavra_buscar}' não foi encontrada no arquivo JSON.")
