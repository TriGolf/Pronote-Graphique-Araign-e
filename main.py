import pronotepy
from pronotepy.ent import ac_orleans_tours
import datetime
import plotly.express as px
import pandas as pd
import getpass

while True :
    try :
        utilisateur = input('Veuillez entrer votre nom d\'utilisateur : ')
        mot_de_passe = getpass.getpass("Veuillez entrer votre mot de passe : ")

        client = pronotepy.Client(
            'https://0450047g.index-education.net/pronote/eleve.html',
            username=utilisateur, # votre identifiant ENT !!!
            password=mot_de_passe, # votre mot de passe
            ent=ac_orleans_tours)
        
        print(f'Vous êtes conncté(e) en tant que {client.info.name} !')
        
        break
    except :
        print("Les identifiants sont invalides, veuillez rééssayer")


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
                    markers = True,text = 'value')


title = f"Moyenne générale : {client.current_period.overall_average}"
max_limit = 20
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, max_limit]
        ),
    ),
    title=title,  # Titre du graphique
    title_x=0.5,  # Position horizontale du titre
    title_y=0.02,  # Position verticale du titre (au-dessus du graphique)
)

fig.update_traces(textposition = 'top center')

fig.show() 


