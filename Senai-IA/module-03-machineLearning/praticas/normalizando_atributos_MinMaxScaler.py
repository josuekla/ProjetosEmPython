# ============================================================
# Exemplo 3: Normalização com MinMaxScaler
# ============================================================
 
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
 
# Criando um DataFrame fictício
dados = pd.DataFrame({
    'temperatura': [75, 80, 79, 82, 77],
    'vibracao': [0.35, 0.50, 0.48, 0.60, 0.40],
    'pressao': [1.2, 1.5, 1.4, 1.7, 1.3]
})
 
print("Dados originais:")
print(dados)
 
# Aplicando MinMaxScaler
scaler = MinMaxScaler()
dados_scaled = scaler.fit_transform(dados)
 
# Convertendo para DataFrame para visualização
dados_scaled_df = pd.DataFrame(dados_scaled, columns=dados.columns)
 
print("\nDados após normalização com MinMaxScaler (intervalo 0 a 1):")
print(dados_scaled_df)

# OUTPUT
# Dados originais:
#    temperatura  vibracao  pressao
# 0           75      0.35      1.2
# 1           80      0.50      1.5
# 2           79      0.48      1.4
# 3           82      0.60      1.7
# 4           77      0.40      1.3

# Dados após normalização com MinMaxScaler (intervalo 0 a 1):
#    temperatura  vibracao  pressao
# 0     0.000000      0.00      0.0
# 1     0.714286      0.60      0.6
# 2     0.571429      0.52      0.4
# 3     1.000000      1.00      1.0
# 4     0.285714      0.20      0.2