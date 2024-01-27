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
from random import randint

num=randint(1,8)

def generer_elements():
    global num
    questions=[]
    #questions+= ["Donner la définition de triangles semblables"]
    #questions+= ["Enoncer le théorème de Thalès"]
    #questions+= ["Enoncer la réciproque du théorème de Thalès"]
    #questions+= ["Donner la définition de l'opposé d'un nombre $n$"]
    #questions+= ["D'après l'identité remarquable, quelle est la version factorisée de $a^2-b^2$ ?"]
    #questions+= ["D'après l'identité remarquable, quelle est la version factorisée de $a^2+ 2ab + b^2$ ?"]
    #questions+= ["D'après l'identité remarquable, quelle est la version factorisée de $a^2 - 2ab + b^2$ ?"]
    #questions+= ["Donner la définition d'un nombre premier"]
    #questions+= ['Que signifie "$a$ est un multiple de $b$" ?']
    #questions+= ['Que signifie "$a$ est un diviseur de $b$" ?']
    questions+=["Soit $a$ un nombre non nul. Quelle est la définition de l'inverse de $a$ ?"]
    questions+= ["Donner la définition d'un événement élémentaire"]
    questions+= ["Donner la définition d'un événement impossible"]
    questions+= ["Si A est un événement, décrire avec des mots ce qu'est l'événement complémentaire de A"]
    questions+= ["Donner la définition d'un événement certain"]
    questions+= ["Donner la définition de deux événements incompatibles"]
    questions+= ["Donner la définition de deux événements contraires"]
    d={"question" : questions[num%(len(questions))]}
    num+=1
    return d



def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)
