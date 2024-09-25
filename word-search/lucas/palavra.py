import json
import os

def read_file(path):
    extension = os.path.splitext(path)[-1].lower()

    if extension == '.txt':
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    elif extension == '.json':
        with open(path,'r', encoding='utf-8') as file:
            return json.load(file)
        
    else:
        print('ferrou meu chapa!')

def word_search(text, word):

    low_text = str(text).lower()
    low_word = word.lower()

    if low_word in low_text:
        print(f'a palavra {low_word} foi encontrada, meu nobre!')
    else:
        print(f'a palavra {low_word} não foi encontrada, meu nobre!')

path = input("Digite o caminho do arquivo: ")
word = input("Digite a palavra que deseja buscar: ")

text = read_file(path)
word_search(text, word)