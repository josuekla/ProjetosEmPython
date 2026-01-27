# ============================================================
# Exemplo: Validação Cruzada com LogisticRegression
# ============================================================
 
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import numpy as np
 
# 1. Criando um DataFrame fictício
dados = pd.DataFrame({
    'temperatura': [75, 80, 79, 82, 77, 85, 83, 76, 81, 78],
    'vibracao': [0.35, 0.50, 0.48, 0.60, 0.40, 0.55, 0.58, 0.38, 0.53, 0.45],
    'pressao': [1.2, 1.5, 1.4, 1.7, 1.3, 1.6, 1.8, 1.2, 1.5, 1.4],
    'falha': [0, 1, 0, 1, 0, 1, 1, 0, 1, 0]  # variável alvo
})
 
print("Dados originais:")
print(dados)
 
# 2. Separando as variáveis independentes (X) e alvo (y)
X = dados[['temperatura', 'vibracao', 'pressao']]
y = dados['falha']
 
# 3. Normalizando as features
scaler = StandardScaler()
X_normalizado = scaler.fit_transform(X)
 
# 4. Criando um modelo de Regressão Logística
modelo = LogisticRegression(max_iter=1000)
 
# 5. Aplicando validação cruzada com 5 folds
scores = cross_val_score(modelo, X_normalizado, y, cv=5)
 
# 6. Exibindo os resultados
print("\nAcurácias obtidas em cada fold:", scores)
print("Acurácia média:", np.mean(scores))