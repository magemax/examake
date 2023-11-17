from template_management import load_template
from random import randint, shuffle, choice


class Expression:
    def __init__(self, question, corrige) -> None:
        self.question=question
        self.corrige= corrige


exprs=[]

exprs+=[Expression(r"10x-12x^2", r"10x-12x^2=2x\times5-2x\times6x=2x(5-6x)")]
exprs+=[Expression(r"5x^2+6x", r"5x^2+6x=x\times 5x+x\times 6=x(5x+6)")]
exprs+=[Expression(r"2x^2+x", r"2x^2+x=x\times 2x+x\times 1=x(2x+1)")]
exprs+=[Expression(r"9x+12x^2", r"9x+12x^2=3x\times3+3x\times4x=3x(3+4x)")]

Q1 = exprs[:]


exprs=[]

exprs+=[Expression(r"35a+45b", r"35a+45b=5\times7a+5\times9b=5(7a+9b)")]
exprs+=[Expression(r"-7a+21b", r"-7a+21b=-7a+7\times3b=7(-a+3b)")]
exprs+=[Expression(r"5a+15b", r"5a+15b=5a+5\times3b=5(a+3b)")]
exprs+=[Expression(r"14a-21b", r"14a-21b=7\times2a-7\times3b=7(2a-3b)")]

Q2 = exprs[:]

exprs=[]

exprs+=[Expression(r"x^2-16", r"x^2-16 = x^2-4^2 = (x-4)(x+4)")]
exprs+=[Expression(r"9x^2-64", r"9x^2-64 = (3x)^2-8^2 = (3x-8)(3x+8)")]
exprs+=[Expression(r"25x^2-1", r"25x^2-1 = \left(5x\right)^2-1^2 = \left(5x-1\right)\left(5x+1\right)")]
exprs+=[Expression(r"x^2-36", r"x^2-36 = x^2-6^2 = (x-6)(x+6)")]

Q3 = exprs[:]

lettres="GHI"

def generer_elements():
    xtouse=[]
    for choosefrom in [Q1,Q2,Q3]:
        xtouse+=[choice(choosefrom)]

    #shuffle
    shuffle(xtouse)
    d={}
    d["questions"] =r"\item "+ f"\n \\item ".join(["$"+lettres[k]+"="+ xtouse[k].question+"$" for k in range(len(xtouse))])
    d["corriges"] = r"\item "+f"\n \\item ".join(["$"+lettres[k]+"="+ xtouse[k].corrige+"$" for k in range(len(xtouse))])
    d["enonce"] = "Factoriser les expressions suivantes."
    return d



def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)