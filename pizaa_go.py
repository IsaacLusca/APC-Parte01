# -*- coding: utf-8 -*-
"""PIZAA GO

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11ql-fku0XBzZZPxHzjFRCATHzAAIFtHo
"""

pip install plotly

import plotly

import plotly.graph_objects as go

labels = ['Agricultura' , 'Bunker Fuels' , 'Industrial Processes' ,'Land-Use Change and Forestry', 'Waste']
values = [5817.65 , 1311.60, 2902.68, 1387.56, 1606.86]


#O pull=[0, 0, 0, 0, 0.2] serve para afastar um pedaço da pizza 


fig = go.Figure(data=[go.Pie(labels=labels, values=values,pull=[0, 0, 0, 0, 0.2])])

#O fig.update_layout(title_text='EMISSÕES DE CO2') serve para da o Titulo do gráfico 

fig.update_layout(title_text='EMISSÕES DE CO2')
fig.show()