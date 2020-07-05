#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np


# In[4]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[212]:


black_friday.head()


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[6]:


def q1():
    return black_friday.shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[211]:


def q2():
    question_2 = black_friday[['Age', 'Gender']]
    valores = question_2.groupby('Gender')['Age'].value_counts()[0]
    return int(valores)


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[99]:


def q3():
    teste = black_friday['User_ID'].unique()
    return len(teste)


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[107]:


def q4():
    return len(black_friday.dtypes.unique())


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[9]:


def q5():
    return float((black_friday.isna().any(axis=1)).mean())


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[138]:


def q6():
    return int(black_friday.isna().sum().max())


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[145]:


def q7():
    return int(black_friday['Product_Category_3'].mode())


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[168]:


def q8():
    base = black_friday['Purchase']
    normalized_df = (base-base.min())/(base.max()-base.min())
    return float(normalized_df.mean())


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[223]:


def q9():
    base = black_friday['Purchase']
    normalized_df = (base-base.min())/(base.max()-base.min())
    return len(normalized_df.unique())


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[32]:


def q10():
    product_2 = black_friday['Product_Category_2'].isna()
    product_3 = black_friday['Product_Category_3'].isna()
    product2_3 = product_2 & product_3
    return bool((product2_3 == product_2).all())

