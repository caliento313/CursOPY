# Passo a passo
# Passo 0 : Entender o desafio e a empresa
# Passo 1 : Importar a base de dados
import pandas
import pandas as pd
from IPython.core.display import display
from sklearn.preprocessing import LabelEncoder
codificador1 = LabelEncoder()


tabela = pandas.read_csv('clientes.csv')
#display(tabela)


#profissao
tabela['profissao'] = codificador1.fit_transform(tabela['profissao'])

#mix_credito
codificador2 = LabelEncoder()
tabela['mix_credito'] = codificador2.fit_transform(tabela['mix_credito'])

#comportamento_pagamento
codificador3 = LabelEncoder()
tabela['comportamento_pagamento'] = codificador3.fit_transform(tabela['comportamento_pagamento'])
#display(tabela.info())

#separar as info de base para a inteligencia artificial
# y -> Quem eu quero prever (coluna score_credito)
# x -> As outras colunas
y = tabela['score_credito']
x = tabela.drop(columns= ['score_credito','id_cliente'])

# Separar os dados de terino e de teste
from sklearn.model_selection import  train_test_split
x_treino, x_teste , y_treino, y_teste = train_test_split(x,y)

#passo 3 -  Criar um modelo de ia -> Prever uma nota de credito
# Importar modelo
from sklearn.ensemble import  RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
# Criar modelo
modelo_arvoredecisao = RandomForestClassifier()
modelo_knn = KNeighborsClassifier()
# Reinar modelo
modelo_arvoredecisao.fit(x_treino, y_treino)
modelo_knn.fit(x_treino, y_treino)

#Passo 4 : Escolher o melhor modelo
# Previsões
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)
previsao_knn = modelo_knn.predict(x_teste)

#acuracia
from sklearn.metrics import  accuracy_score

#display(accuracy_score(y_teste, previsao_arvoredecisao))
#display(accuracy_score(y_teste, previsao_knn))

# Passo 5 : Fazer novas previsões
# Melhor modelo é o de arvore de decisao

# mmodelo_arvoredecisao
tabela_nova = pd.read_csv('novos_clientes.csv')
display(tabela_nova)
#profissao
tabela_nova['profissao'] = codificador1.fit_transform(tabela_nova['profissao'])
#mix_credito
tabela_nova['mix_credito'] = codificador2.fit_transform(tabela_nova['mix_credito'])
#comportamento_pagamento
tabela_nova['comportamento_pagamento'] = codificador3.fit_transform(tabela_nova['comportamento_pagamento'])

previsao = modelo_arvoredecisao.predict(tabela_nova)
display(previsao)







