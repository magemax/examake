# Exercice : Donner une liste de 15 entiers, déterminer les nombres premiers
# 0, 1, 2, 3, 4, 5  ===>  3 parmi 6
# Entre 6 et 50 ===> 7
# 50 ou + ===>   5
# Exercice : Donner une liste de 15 entiers, déterminer les nombres premiers
# 0, 1, 2, 3, 4, 5  ===>  3 parmi 6
# Entre 6 et 50 ===> 7
# 50 ou + ===>   5
from template_management import load_template
from random import sample, shuffle

def generer_elements():
    maxprime=100
    areprime=[0,0]+[1]*(maxprime-2)
    for i in range(2,maxprime):
        if areprime[i]:
            print(i)    
            ii=i+i
            while ii<maxprime:
                areprime[ii]=0
                ii+=i
    
    listeprems=sample([0,1,2,3,4,5], 3)
    autreliste=sample(list(range(7,50,2))+list(range(14,28,4)),6)
    listeprems += autreliste
    autreliste=sample(list(range(51,100,2)),3)
    listeprems += autreliste
    shuffle(listeprems)
    d={}
    d["liste_sujet"] = " { } ".join([str(k) for k in listeprems])
    d["liste_corrige"] = " { } ".join([r"\underline{"+str(k)+r"}" if areprime[k] else str(k) for k in listeprems])
    return d



def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)
