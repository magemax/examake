from template_management import load_template

from random import randint, sample, choice
from scipy.interpolate import lagrange
import numpy as np
from numpy.polynomial.polynomial import Polynomial
import matplotlib.pyplot as plt





def random_texte(p=0):#Avec les mots à remplacer
    if p==0:
        l1_intro = "Vous écrivez une lettre à votre tante, qui se remet d'une rage de dents. Complétez les mots que vous avez oubliés"
        l1_texte = r"""\frenchcursive{ Très chère Tante, j'ai bien terminé mon premier mois de 3ème au collège Paul Bert ! En mathématiques, nous avons vu les fonctions.
        Une fonction est une machine qui transforme un nombre en un autre. 
        """ + "\n\n" + choice([r"""Par exemple, si une fonction qui s'appelle $f$ transforme {w_ant} en {w_img}, 
        alors on note que  $f({w_ant_h}) = {w_img_h}$ (En fait, on prononce {w_prononciation}).""",
            r"""Par exemple, si on a $f({w_ant_h}) = {w_img_h}$  (on prononce {w_prononciation}), cela veut dire qu'une fonction qui s'appelle $f$ prend le nombre {w_ant_h} et renvoie le nombre {w_img_h}.""",
            ]) + "\n\n"+ choice([r"""On dit aussi que {w_ant} est l'{w_ant_mot} de {w_img} par f,  et {w_img} l'{w_img_mot} de {w_ant}. """, r"""On dit aussi que {w_img} est l'{w_img_mot} de {w_ant} par f,  et {w_ant} l'{w_ant_mot} de {w_img}. """]) + choice(
                [r"""Ah, j'oubliais, on peut aussi les dessiner : puisque {w_img} est l'{w_img_mot} de {w_ant}, alors on dessinera sur la courbe le point $A({w_ant_h};{w_img_h})$ : 
        Quand je regarde le graphe, je peux lire la valeur d'entrée dans la fonction sur l'axe des {w_abs_mot}, et sa valeur de sortie sur l'axe des {w_ord_mot}""",
            r"""Ah, j'oubliais, on peut aussi les dessiner : puisque {w_ant} est l'{w_ant_mot} de {w_img}, alors on dessinera sur la courbe le point $A({w_ant_h};{w_img_h})$. 
            Quand je regarde le graphe, je peux lire la valeur d'entrée dans la fonction sur l'axe des {w_abs_mot}, et sa valeur de sortie sur l'axe des {w_ord_mot}"""
        ]) + """\n\nJ'espère que toi et tes dents allez mieux !""" + "}"
    if p==1:
        l1_intro = "Complétez le texte ci-dessous avec le vocabulaire et les notations des fonctions"
        l1_texte = r"""Une fonction est un objet mathématique qui prend un nombre entrée et le transforme en un nombre de sortie. 
        """ + "\n\n" + choice([r"""Par exemple, si une fonction $f$ prend {w_ant} en entrée et renvoie {w_img} en sortie, 
        on le note $f({w_ant_h}) = {w_img_h}$ (Et on prononce {w_prononciation}).""",
            r"""Par exemple, si on a $f({w_ant_h}) = {w_img_h}$  (on prononce {w_prononciation}), 
            cela veut dire qu'une fonction $f$ renvoie le nombre {w_img_h} quand on lui donne en entrée le nombre {w_ant_h}.""",
            ]) + "\n\n"+ choice([r"""On dit que {w_ant} est l'{w_ant_mot} de {w_img} par $f$,  et {w_img} l'{w_img_mot} de {w_ant} par $f$. """,
             r"""On appelle {w_img} l'{w_img_mot} de {w_ant} par la fonction f,  et {w_ant} l'{w_ant_mot} de {w_img} par f. """]) + choice(
                [r"""On présente parfois des valeurs prises par une fonction dans un tableau de valeur. Dans notre exemple, comme {w_img} est l'{w_img_mot} de {w_ant}, on écrit dans une colonne le nombre {w_ant_h} sur la première ligne du tableau, 
                et {w_img_h} sur la deuxième ligne. """,
                r"""On présente parfois des valeurs prises par une fonction dans un tableau de valeur. Dans notre exemple, comme {w_ant} est l'{w_ant_mot} de {w_img}, on écrit dans une colonne le nombre {w_ant_h} sur la première ligne du tableau, 
                et {w_img_h} sur la deuxième ligne. """,])
    if p==2:
        l1_intro = "Votre petite cousine a du mal à dormir, et vous lui racontez une histoire sur les fonctions. Complétez les parties manquantes du texte sans erreur."
        l1_texte = r""" "Le héros de mon histoire est une fonction qui s'appelle $f$, et qui, comme toutes les fonctions, transforme un nombre en un autre. Mais $f$ le fait d'une manière bien à elle, elle {w_rajenl} toujours la même valeur à la valeur d'entrée pour obtenir la valeur de sortie.
        
        
        """ + choice([r"""Mais ce matin, elle reçoit en entrée le nombre {w_ant} et se rend compte qu'elle renvoie le nombre {w_img}.""",
            r"""Mais aujourd'hui, elle obtient comme valeur de sortie {w_img}, et se souvient qu'on avait donné en valeur d'entrée {w_ant}."""
        ]) + "\n\n" + r"""Cela veut dire qu'on peut noter $f({w_ant_h}) = {w_img_h}$ (que vous prononcez {w_prononciation}). 
        """ + choice([r"""On dit aussi que {w_ant} est l'{w_ant_mot} de {w_img} par $f$,  et {w_img} l'{w_img_mot} de {w_ant}. """,
            r"""On dit aussi que {w_img} est l'{w_img_mot} de {w_ant} par $f$,  et {w_ant} est l'{w_ant_mot} de {w_img}. """
            ]) + "\n\n" + r"""Avec cette information, $f$ peut enfin connaître sa formule : Puisqu'elle a transformé {w_ant_h} en {w_img_h}, elle sait enfin ce qu'elle fait : elle {w_rajenl} toujours le même nombre au nombre de départ, et ce nombre est {w_absab_h} ! 
        Cela veut dire qu'elle sait comment on écrit sa fonction en fonction de $x$, son écriture préférée. C'est {w_ecriture_formule} .  $f$ commence à dessiner sa courbe représentative et se rend compte que ..."
        
        Mais vous vous rendez-compte que votre petite cousine s'est endormie. Elle sourit. vous finirez votre histoire plus tard..."""

    return {"intro": l1_intro, "body": l1_texte}


def generer_elements(): #Renvoie un dictionnaire qui contient tous les mots qui apparaissent dans le template. 
    
    num_texte=randint(0,2)
    dd_b=random_texte(num_texte)
    #On remplit les trous
    ant, img = sample(range(1,10),2)

    toreplace={"ant": str(ant), "img": str(img)}
    if ant<img:
        toreplace["rajenl"]= "rajoute"
    else:
        toreplace["rajenl"]= "enlève"
    toreplace["absab_h"]=r"\Texteoulongueur{" +str(abs(ant-img))+"}{0.7}"
    formule =f"x {'+' if img>ant else'-'}{abs(ant-img)}"
    toreplace["ecriture_formule"] = r"$f(x)=\Texteoulongueur{" + formule + "}{2}$"
    toreplace["ant_h"]=r"\Texteoulongueur{" + str(ant) + r"}{0.7}"
    toreplace["img_h"]=r"\Texteoulongueur{" + str(img) + r"}{0.7}"
    toreplace["prononciation"]=r'"\Texteoulongueur{f de ' + str(ant)+r'}{2} égale '+toreplace["img_h"]+'"'
    toreplace["img_mot"]=r"\Texteoulongueur{image}{3.5}"
    toreplace["ant_mot"]=r"\Texteoulongueur{antécédent}{3.5}"
    toreplace["abs_mot"]=r"\Texteoulongueur{abscisses}{3.5}"
    toreplace["ord_mot"]=r"\Texteoulongueur{ordonnées}{3.5}"
    
    for k,v in toreplace.items():
        dd_b["body"] = dd_b["body"].replace("{w_"+k+'}', v)
    return dd_b

#Fonction qui prend le template, et 

def build(**args): 
    print(args)
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)