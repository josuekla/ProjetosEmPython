	# ============================================================
# Exemplo 2: Normalização com StandardScaler
# ============================================================
 
import pandas as pd
from sklearn.preprocessing import StandardScaler
 
# Criando um DataFrame fictício
dados = pd.DataFrame({
    'temperatura': [75, 80, 79, 82, 77],
    'vibracao': [0.35, 0.50, 0.48, 0.60, 0.40],
    'pressao': [1.2, 1.5, 1.4, 1.7, 1.3]
})
 
print("Dados originais:")
print(dados)
 
# Aplicando StandardScaler
scaler = StandardScaler()
dados_scaled = scaler.fit_transform(dados)
 
# Convertendo para DataFrame para visualização
dados_scaled_df = pd.DataFrame(dados_scaled, columns=dados.columns)
 
print("\nDados após normalização com StandardScaler (média=0, desvio=1):")
print(dados_scaled_df)


# OUTPUT
# Dados originais:
#    temperatura  vibracao  pressao
# 0           75      0.35      1.2
# 1           80      0.50      1.5
# 2           79      0.48      1.4
# 3           82      0.60      1.7
# 4           77      0.40      1.3

# Dados após normalização com StandardScaler (média=0, desvio=1):
#    temperatura  vibracao   pressao
# 0    -1.489691 -1.346291 -1.278724
# 1     0.579324  0.394603  0.464991
# 2     0.165521  0.162483 -0.116248
# 3     1.406930  1.555198  1.627467
# 4    -0.662085 -0.765993 -0.697486