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
    
    questions=[]
    questions+= ["Donner la définition de triangles semblables"]
    questions+= ["Enoncer le théorème de Thalès"]
    questions+= ["Enoncer la réciproque du théorème de Thalès"]
    questions+= ["Donner la définition de l'opposé d'un nombre $n$"]
    questions+= ["D'après l'identité remarquable, quelle est la version factorisée de $a^2-b^2$ ?"]
    questions+= ["D'après l'identité remarquable, quelle est la version factorisée de $a^2+ 2ab + b^2$ ?"]
    questions+= ["D'après l'identité remarquable, quelle est la version factorisée de $a^2 - 2ab + b^2$ ?"]
    #questions+= ["Donner la définition d'un nombre premier"]
    #questions+= ['Que signifie "$a$ est un multiple de $b$" ?']
    #questions+= ['Que signifie "$a$ est un diviseur de $b$" ?']
    d={"question" : choice(questions)}
    return d



def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)
