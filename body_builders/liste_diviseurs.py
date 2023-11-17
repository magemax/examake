# Exercice : Donner une liste de 15 entiers, déterminer les nombres premiers
# 0, 1, 2, 3, 4, 5  ===>  3 parmi 6
# Entre 6 et 50 ===> 7
# 50 ou + ===>   5
# Exercice : Donner une liste de 15 entiers, déterminer les nombres premiers
# 0, 1, 2, 3, 4, 5  ===>  3 parmi 6
# Entre 6 et 50 ===> 7
# 50 ou + ===>   5
from template_management import load_template
from random import choice

def generer_elements():
    nombre = choice([60, 90, 84, 126, 150, 140])

    listdivs=[]
    for i in range(1,nombre+1):
        if nombre%i==0:
            listdivs+=[i]
    d={}
    d["nombre"]=nombre
    d["listdivs"]=" { } ".join([str(k) for k in listdivs])
    return d



def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)
