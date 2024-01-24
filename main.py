import pronotepy
from pronotepy.ent import ac_orleans_tours
import datetime
import plotly.express as px
import pandas as pd

client = pronotepy.Client(
    'https://0450047g.index-education.net/pronote/eleve.html',
    username='nom d\'utilisateur', # votre identifiant ENT !!! ex : p.nomX
    password="mot de passe", # votre mot de passe
    ent=ac_orleans_tours)


subjects = []
averages = []
class_averages = []


for moyenne in client.current_period.averages :
    averages.append(moyenne.student)
    subjects.append(moyenne.subject.name)


def convert(liste) :
    for l in range(len(liste)) :
        liste[l] = liste[l].replace(',','.')
        nb = float(liste[l])
        liste[l] = nb
    return liste

averages = convert(averages)
df = pd.DataFrame(dict(
    value = averages,
    variable = subjects))
           
fig = px.line_polar(df, r = 'value', theta = 'variable', line_close = True,
                    markers = True)

fig.update_layout(polar=dict(
    radialaxis = dict(
        visible=True,
        range[0,max_limit]
    )
))

fig.show()

