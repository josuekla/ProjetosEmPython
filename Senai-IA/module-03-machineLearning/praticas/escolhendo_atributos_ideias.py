import pandas as pd
 
# Criando um DataFrame fictício com dados de sensores
dados = pd.DataFrame({
    'id_sensor': [101, 102, 103, 104, 105],
    'data': ['2025-07-29', '2025-07-29', '2025-07-29', '2025-07-29', '2025-07-29'],
    'temperatura': [75, 80, 79, 82, 77],
    'vibracao': [0.35, 0.50, 0.48, 0.60, 0.40],
    'pressao': [1.2, 1.5, 1.4, 1.7, 1.3],
    'falha': [0, 1, 0, 1, 0]
})
 
# Exibindo o DataFrame original
print("DataFrame original com todas as colunas:")
print(dados)
 
# Selecionando apenas as colunas mais relevantes para o modelo
colunas_relevantes = ['temperatura', 'vibracao', 'pressao']
dados_filtrados = dados[colunas_relevantes]
 
# Exibindo o DataFrame após a seleção de atributos
print("\nDataFrame após selecionar apenas as colunas relevantes:")
print(dados_filtrados)