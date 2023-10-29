from template_management import load_template

import body_builders.thales_normal
import body_builders.thales_indirect
from random import choice

def generer_elements():
    imgs1=["../../assets/images/thales_annales/"+ f'img1{k}.png' for k in range(1,5)]
    imgs2=["../../assets/images/thales_annales/"+ f'img2{k}.png' for k in range(1,4)]
    numim1=choice(list(range(4)))
    numim2=choice(list(range(3)))

    q1vf=r"""Dites si l'affirmation ci-dessous est vraie ou fausse, \textbf{en justifiant votre réponse}."""
    q1qcm=r"""Choisissez la bonne réponse parmi celles proposées, \textbf{en justifiant votre réponse}."""
    d={}

    d["img1"]=imgs1[numim1]
    d["question1"]=q1vf if d["img1"]!=2 else q1qcm
    d["img2"]=imgs2[numim2]
    d["question2"]=r"""Résoudre le problème suivant \textbf{en expliquant votre raisonnement.}"""
    return d


def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)