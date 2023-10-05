
from random import randint, sample, choice, shuffle
from fractions import Fraction
from template_management import load_template

def to_latex(frac):
    return f"\\frac{{{frac.numerator}}}{{{frac.denominator}}}"

def affine_to_latex(a,b): #fonction ax+b
    if a==0:
        raise "Non mais faut pas déconner je suis pas l'armée du salut"
    if abs(a)==1:
        if a>0:
            f="x"
        else:
            f="-x"
    else:
        f=f"{a}x"
    if b>0:
        f+=f"+{abs(b)}"
    elif b<0:
        f+=f"-{abs(b)}"
    return f
        

def generer_elements():
    #Programme : 
    # a(x+b) + c
    a=randint(2,9)
    b=randint(3,6)*choice([-1,1])
    c=-a*b
    while c==-a*b or c==b:
        c=randint(3,6)*choice([-1,1])
    steps = [f"Lui {'ajouter' if b>0 else 'retrancher'} {abs(b)}",
            f"Multiplier le résultat par {a}",
            f"{'Ajouter' if c>0 else 'Retrancher'} {abs(c)} au résultat",
            ]
    def h(x):
        return a*(x+b)+c
    d={}
    d["formule"]=affine_to_latex(a, a*b+c)
    d["items_programme"] = r"\item " + "\n \\item ".join(steps)
    d["antecedent1"]=randint(max(1,-b+1), 12)
    d["image1"]=h(d["antecedent1"])
    d["antecedent1b"]=randint(-10,-3)
    d["image1b"]=h(d["antecedent1"])
    antec1c=1
    while antec1c==int(antec1c):
        antec1c=Fraction(randint(1,3),randint(2,9))
    im1c=h(antec1c)
    d["antecedent1c"]=to_latex(antec1c)
    d["image1c"]=to_latex(im1c)
    
    autreantec = choice(list([k for k in range(-9,10) if k and k!=d["antecedent1"]]))
    d["image3"]=h(autreantec)
    d["antec3"]=autreantec

    return d



def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)