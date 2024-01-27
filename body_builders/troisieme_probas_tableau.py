from template_management import load_template
from random import randint,sample, shuffle, choice
from fractions import Fraction



def fraction_to_latex(f):
    if f.denominator ==1:
        return str(f.numerator)
    else:
        return f"\\frac{{{f.numerator}}}{{{f.denominator}}}"

numb=0


def generer_elements():
    tc = choice([ 19,23, 29, 31, 37])
    a,b,c,d=[randint(4,12) for i in range(4)]
    while a+b+c+d !=tc:
        a,b,c,d=[randint(4,12) for i in range(4)]
    
    Carac = [["sont des garçons", "sont des filles"]]
    Carac += [["mangent à la cantine", "sont externes"]]
    Carac += [["aiment les probabilités", "préfèrent la géométrie"]]
    Carac += [["ont des lunettes", "n'ont pas de lunettes"]]
    Carac += [["ont amené un livre au TLML", "n'ont pas amené de livre au TLML"]]

    c1,c2=sample(Carac,2)

    Debut = f"Dans une classe de {tc} élèves : \n"
    Debut += r"\begin{itemize}" +"\n"
    Debut+= fr"\item {a+b} {c1[0]}, les autres {c1[1]}" +"\n"
    Debut+= fr"\item {a+c} {c2[0]}, les autres {c2[1]}" +"\n"
    given, asked = sample([0,1,2,3],2)
    posses= [f"{c1[0]} et {c2[0]}", f"{c1[0]} et {c2[1]}", f"{c1[1]} et {c2[0]}", f"{c1[1]} et {c2[1]}"] 
    Debut += fr"\item {[a,b,c,d][given]} {posses[given]}" +"\n"
    Debut += r"\end{itemize}" +"\n \n"

    Debut += r"\begin{enumerate}" +"\n"
    Debut += fr"\item \`A l'aide d'un tableau à double entrée, représenter les effectifs de toutes les combinaisons possibles des deux caractéristiques présentées."
    Debut += fr"\item  On tire au hasard un élève de la classe. Quelle est la probabilité qu'on tombe sur :"
    Debut += r"\begin{enumerate}" +"\n"
    Debut += fr"\item un des élèves qui {choice([c1[0]])} ?"
    Debut += fr"\item un des élèves qui {choice([c2[1]])} ?"
    Debut += fr"\item un des élèves qui {posses[asked]} ?"
    Debut += r"\end{enumerate}" +"\n"
    Debut += r"\end{enumerate}" +"\n \n"
    
    d={}
    d["question"] = Debut
    d["full_corrige"] = "Pas (encore) de corrigés, faites l'exercice"
    return d


def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)