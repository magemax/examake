from template_management import load_template
from random import randint,sample, shuffle, choice
from fractions import Fraction


numb=0


def generer_elements():
    d={}
    d["question"] = r"""On rappelle le résultat du cours qu'on pourra utiliser sans justification :  pour des nombres non nuls $p,q,r,s$, $\dfrac{p}{q} = \dfrac{r}{s}$ si et seulement si $ps = qr$.
    
    Dans cet exercice, $a,b,c$ et $d$ sont quatre nombres entiers strictement positifs et tous différents.
    \begin{enumerate}
        \item Montrer que si $\dfrac{a}{b} = \dfrac{c}{d}$, alors $\dfrac{a+c}{b +d} = \dfrac{a}{b}$        
        \item Montrer que si $\dfrac{a+c}{b+d} = \dfrac{a}{b}$, alors $\dfrac{a}{b} = \dfrac{c}{d}$        
    \end{enumerate}
    """
    d["full_corrige"] = "TBD"
    return d


def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)