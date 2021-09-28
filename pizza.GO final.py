# -*- coding: utf-8 -*-
"""Olá, este é o Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

import plotly
import plotly.graph_objects as go
import pandas as pd

#As linhas de codigo a baixo serve para trazer a base de dados e realizar sua leitura
base = pd.read_csv('https://raw.githubusercontent.com/EdPPF/APC-Parte01/main/co2-emissions-by-fuel-line_1.csv')

base_array = base.values

#A função a baixo serve para coletar os elementos da base de dados e transformar em listas para facilitar a manipulação 
paises = []
anos = []
oleo = []
queimada = []
cement = []
carvao = []
gas = []
for elemento in base_array:
    paises.append(elemento[0])
    anos.append(elemento[2])
    oleo.append(elemento[3])
    queimada.append(elemento[4])
    cement.append(elemento[5])
    carvao.append(elemento[6])
    gas.append(elemento[7])

listas = [paises, anos, oleo, queimada, cement, carvao, gas]

#a função a baixo serve para deletar os elemenstos da base de dados  que não irei ultilizar

for lista in listas:
    del lista[:3210]
    del lista[29:5130]
    del lista[58:3539]
    del lista[87:6808]
    del lista[116:3597]
    del lista[145:19016]
    del lista[174:11485]
    del lista[203:8004]
    del lista[232:]



#media das emissoes do gas
SG = 0

for nota in gas:
    SG += nota

MG = int(SG)/232
#media das emissoes do carvao
SC = 0

for nota in carvao:
    SC += nota

MC = int(SC)/232
#media das emissoes do cement
SCMT = 0

for nota in gas:
    SCMT += nota

MCMT = int(SCMT)/232
#media das emissoes do queimada
SQ = 0

for nota in gas:
    SQ += nota

MQ = int(SQ)/232

#media das emissoes do OLEO
SO = 0

for nota in gas:
    SO += nota

MO = int(SO)/232

Values = [MG , MC , MCMT , MQ , MO]

labels = ['Gasolina' , 'Carvão',  'Cimento' ,'Queimadas', 'óleo']

#O pull=[0, 0, 0, 0, 0.2] serve para afastar um pedaço da pizza 


fig = go.Figure([go.Pie(labels=labels, values=Values,pull=[0, 0, 0.2, 0, 0,])])

# O codigo a baixo serve para personalizar o gráfico 
colors = ['gold', 'Crimson', 'LightSlateGray', 'Black', 'Chartreuse']

#textfont_size = fonte do grãfico ,marker=dict(colors=colors = definir cores de cada pedaço 
# line=dict( color='#4169E1',width=2 )  Colorir as divisoes do grafico 

fig.update_traces(textfont_size=15, marker=dict(colors=colors, line=dict( color='#4169E1',width=2 ) ))


#O fig.update_layout(title_text='EMISSÕES DE CO2 NOS SETORES DE COMBUSTÍVEIS') serve para da o Titulo do gráfico 

#template = 'plotly_dark' deixar o grafico em modo escuro 

fig.update_layout(title_text='EMISSÕES DE CO2 NOS SETORES DE COMBUSTÍVEIS', template = 'plotly_dark')
fig.show()