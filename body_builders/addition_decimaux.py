from template_management import load_template

from random import randint, sample, choice


def generer_elements():
    question = [r"""Calculer, en posant l'opération si nécessaire :
        \begin{enumerate}
            \begin{multicols}{2}"""]

    #Deux additions et deux soustraction de decimaux.
    # 3-4 chiffres
    a,b=0,0
    while a%10==0:
        a=randint(100,999)
    while b%10==0:
        b=randint(100,999)
    
    res=a+b*10
    aa= str(a)
    aa=aa[:-2]+"{,}"+aa[-2:]
    bb=str(b)
    bb=bb[:-1]+"{,}"+bb[-1:]
    cc=str(res)
    cc=cc[:-2]+"{,}"+cc[-2:]
    
    aa,bb=sample([aa,bb],2)

    question+=[fr"\item ${aa} + {bb} = \Texteouvide{{{cc}}} $"]

# 5-6 chiffres
    a,b=0,0
    while a%10==0:
        a=randint(1000,99999)
    while b%10==0 or "0" not in str(b):
        b=randint(1000,99999)
    nbz=sample([1,2,3],2)
    nbzz= max(nbz)
    nbzm=min(nbz)
    res=(a*(10**nbz[1])+b*(10**nbz[0]))//(10**nbzm)
    aa,bb=sample([aa,bb],2)

    aa= str(a)
    aa=aa[:-nbz[0]]+"{,}"+aa[-nbz[0]:]
    bb=str(b)
    bb=bb[:-nbz[1]]+"{,}"+bb[-nbz[1]:]
    cc=str(res)
    cc=cc[:-nbzz]+"{,}"+cc[-nbzz:]
    question+=[fr"\item ${aa} + {bb} = \Texteouvide{{{cc}}} $"]
    
    # Entier moins decimal à 1 chiffre

    a,b= 0, 50
    while a*10<=b or b%10==0:
        a=randint(1,9)
        b=randint(10,99)

    res=a*10-b
    aa=str(a)
    bb=str(b)
    bb=bb[:-1]+"{,}"+bb[-1:]
    cc=str(res)
    cc=cc[:-1]+"{,}"+cc[-1:]
    question+=[fr"\item ${aa} - {bb} = \Texteouvide{{{cc}}} $"]
    
    # Soustraction

    a,b=0,0
    while a%10==0 or b%10==0 or "0" not in str(a) or a*10**nbz[1] <= b * 10**nbz[0]:
        a=randint(1000,99999)
        b=randint(1000,99999)    
        nbz=sample([1,2,3],2)
    nbzz= max(nbz)
    nbzm=min(nbz)
    res=(a*(10**nbz[1])-b*(10**nbz[0]))//(10**nbzm)
    
    aa= str(a)
    aa=aa[:-nbz[0]]+"{,}"+aa[-nbz[0]:]
    bb=str(b)
    bb=bb[:-nbz[1]]+"{,}"+bb[-nbz[1]:]
    cc=str(res)
    cc=cc[:-nbzz]+"{,}"+cc[-nbzz:]
    question+=[fr"\item ${aa} - {bb} = \Texteouvide{{{cc}}} $"]


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