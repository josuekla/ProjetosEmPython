# Importando bibliotecas
import pandas as pd
import json
 
# --- Lendo dados de um arquivo CSV ---
# Exemplo: dados coletados dos sensores da linha de produção
dados_csv = pd.read_csv('dados_sensores.csv')
print("Primeiras linhas do CSV:")
print(dados_csv.head())
 
# --- Lendo dados de um arquivo JSON ---
# JSON é usado quando os dados possuem estrutura hierárquica
with open('dados_sensores.json') as f:
    dados_json = pd.DataFrame(json.load(f))
 
print("\nPrimeiras linhas do JSON:")
print(dados_json.head())