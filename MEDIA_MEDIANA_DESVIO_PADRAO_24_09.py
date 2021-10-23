#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


temperaturas = [37.5, 38.0, 37.8, 38.5, 37.0, 38.2, 38.8, 37.6, 37.0]
serie = pd.Series(temperaturas)
# verificar a tendência central de valores em conjuntos de dados
media = serie.mean()
mediana = serie.median()

# medida de distância entre valres de umconjunto e a média
variancia = serie.var()

# Indica o valor padrão para os valores de um conjunto (discrepância)
# Qualquer valor acima da média somado com o desvio padrao ou
#Qualquer valor abaixo da média subtraído com o desvio padrão
# É UM VALOR DISCREPANTE!!!!
desvio_padrao = serie.std()

print("Média: ", media)
print("Mediana: ", mediana)
print("Variância: ", variancia)
print("Desvio Padrão: ", desvio_padrao)


# In[ ]:




