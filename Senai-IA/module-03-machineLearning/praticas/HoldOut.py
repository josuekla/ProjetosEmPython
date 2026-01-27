# ============================================================
# Exemplo 4: Divisão de dados com HoldOut (80% treino e 20% teste)
# ============================================================
 
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
 
# 1. Criando um DataFrame fictício
dados = pd.DataFrame({
    'temperatura': [75, 80, 79, 82, 77, 85, 83, 76, 81, 78],
    'vibracao': [0.35, 0.50, 0.48, 0.60, 0.40, 0.55, 0.58, 0.38, 0.53, 0.45],
    'pressao': [1.2, 1.5, 1.4, 1.7, 1.3, 1.6, 1.8, 1.2, 1.5, 1.4],
    'falha': [0, 1, 0, 1, 0, 1, 1, 0, 1, 0]  # variável alvo
})
 
print("DataFrame original:")
print(dados)
 
# 2. Separando features (X) e alvo (y)
X = dados[['temperatura', 'vibracao', 'pressao']]
y = dados['falha']
 
# 3. Normalizando as variáveis independentes
scaler = StandardScaler()
X_normalizado = scaler.fit_transform(X)
 
# 4. Divisão HoldOut: 80% treino, 20% teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X_normalizado, y, test_size=0.2, random_state=42)
 
# 5. Exibindo tamanhos das divisões
print("\nTamanho do conjunto de treino:", len(X_treino))
print("Tamanho do conjunto de teste:", len(X_teste))
 
# Exibindo as primeiras linhas para conferência
print("\nPrimeiras linhas do conjunto de treino (X):")
print(X_treino[:3])
print("\nPrimeiras linhas do conjunto de teste (X):")
print(X_teste[:3])