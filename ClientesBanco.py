# Passo a passo
# Passo 0 : Entender o desafio e a empresa
# Passo 1 : Importar a base de dados
import pandas
from IPython.core.display import display
from sklearn.preprocessing import LabelEncoder
codificador1 = LabelEncoder()


tabela = pandas.read_csv('clientes.csv')
display(tabela)


#profissao
tabela['profissao'] = codificador1.fit_transform(tabela['profissao'])

#mix_credito
codificador2 = LabelEncoder()
tabela['mix_credito'] = codificador2.fit_transform(tabela['mix_credito'])

#comportamento_pagamento
codificador3 = LabelEncoder()
tabela['comportamento_pagamento'] = codificador3.fit_transform(tabela['comportamento_pagamento'])
display(tabela.info())

#separar as info de base para a inteligencia artificial
# y -> Quem eu quero prever (coluna score_credito)
# x -> As outras colunas
y = tabela['score_credito']
x = tabela.drop(columns= ['score_credito','id_cliente'])

# Separar os dados de terino e de teste