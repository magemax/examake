from template_management import load_template

from random import randint, sample, choice
from math import gcd


def generer_elements():
    question = [r"""Calculer, en posant l'opération si nécessaire :
        \begin{enumerate}
            \begin{multicols}{2}"""]

    #Produit d'un entier par une fraction : easy
    # 3-4 chiffres
    a,b,c= 10,10,10
    while gcd(a*b,c) !=1:
        a=randint(2,9)
        b=randint(3,12)
        c=randint(2,42)
    
    question+=[fr"\item ${a} \times \dfrac{{{b}}}{{{c}}} = \Texteouvide{{\dfrac{{{a} \times {b}}}{{{c}}}=\dfrac{{ {a*b} }} {{ {c} }} }} $"]
    
# 1 x 5 chiffres
    a,b=0,0
    while a%10==0:
        a=randint(3,9)
    while b%10==0:
        b=randint(1000,99999)
    nbz=randint(1,3)

    res=a*b

    aa= str(a)
    bb=str(b)
    bb=bb[:-nbz]+"{,}"+bb[-nbz:]

    aa,bb=sample([aa,bb],2)

    cc=str(res)
    cc=cc[:-nbz]+"{,}"+cc[-nbz:]
    question+=[fr"\item ${aa} \times {bb} = \Texteouvide{{{cc}}} $"]
    
# 1 x 5 chiffres
    a,b=0,0
    while a%10==0:
        a=randint(3,9)
    while b%10==0:
        b=randint(1000,99999)
    nbz=randint(1,3)

    res=a*b

    aa= str(a)
    bb=str(b)
    bb=bb[:-nbz]+"{,}"+bb[-nbz:]

    aa,bb=sample([aa,bb],2)

    cc=str(res)
    cc=cc[:-nbz]+"{,}"+cc[-nbz:]
    question+=[fr"\item ${aa} \times {bb} = \Texteouvide{{{cc}}} $"]
    
# 1 x 5 chiffres
    a,b=0,0
    while a%10==0:
        a=randint(21,99)
    while b%10==0:
        b=randint(1000,99999)
    nbz=randint(1,3)
    res=a*b
    aa= str(a)
    bb=str(b)
    bb=bb[:-nbz]+"{,}"+bb[-nbz:]
    aa,bb=sample([aa,bb],2)
    cc=str(res)
    cc=cc[:-nbz]+"{,}"+cc[-nbz:]
    question+=[fr"\item ${aa} \times {bb} = \Texteouvide{{{cc}}} $"]

    question+=[r"""
            \end{multicols}
        \end{enumerate}
    
    """]
    return {"question" : "\n".join(question), "full_corrige" : ""}

def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)