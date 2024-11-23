import pandas as pd

# Carregar o arquivo Excel (colocando o caminho para o arquivo no notebook)
file_path = 'Restaurants That Sell Burritos and Tacos in the U.S.xlsx'

# Carregar todas as planilhas do arquivo Excel
data = pd.read_excel(file_path, None)  # None carrega todas as planilhas como dicionário

# Exibir os nomes das planilhas
sheet_names = data.keys()
print("Nomes das planilhas:", sheet_names)

# Carregar uma planilha específica (por exemplo, a primeira)
df = data[list(sheet_names)[0]]

# Exibir as primeiras linhas do DataFrame
print(df.head())