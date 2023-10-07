
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
    formx=["x"]
    formx+=[f"{formx[-1]} {'+' if b>0 else ''}{b}"]
    formx+=[f"{a}({formx[-1]})"]
    formx+=[f"{formx[-1]}{'+' if c>0 else ''}{c}"]


    steps = [f"Lui {'ajouter' if b>0 else 'retrancher'} {abs(b)}",
            f"Multiplier le résultat par {a}",
            f"{'Ajouter' if c>0 else 'Retrancher'} {abs(c)} au résultat",
            ]
    def h(x):
        return a*(x+b)+c
    d={}
    onecrit = [f"\item Après {k} étape{'s' if k>1 else ''}, ${formx[k]}$" for k in range(len(formx))]
    d["etapes_x"] = "\n".join(onecrit)
    d["formule"]=affine_to_latex(a, a*b+c)
    d["items_programme"] = r"\item " + "\n \\item ".join(steps)
    d["antecedent1"]=randint(max(1,-b+1), 12)
    d["image1"]=h(d["antecedent1"])
    d["form1"]=formx[-1].replace("x",str(d["antecedent1"]))
    d["antecedent1b"]=randint(-10,-3)
    d["image1b"]=h(d["antecedent1b"])
    antec1c=1
    while antec1c==int(antec1c):
        antec1c=Fraction(randint(1,3),randint(2,9))
    im1c=h(antec1c)
    d["antecedent1c"]=to_latex(antec1c)
    d["image1c"]=to_latex(im1c)

    formuledev=[formx[-1]]
    formuledev+=[f"{affine_to_latex(a, a*b)}{'+' if c>0 else ''}{c}"]
    formuledev+=[f"{affine_to_latex(a, a*b+c)}"]
    d["calculformule"]="$"+"=".join(formuledev)+"$"

    autreantec = choice(list([k for k in range(-9,10) if k and k!=d["antecedent1"]]))
    d["image3"]=h(autreantec)
    d["antec3"]=autreantec

    steps = [f"Lui {'ajouter' if b>0 else 'retrancher'} {abs(b)}",
            f"Multiplier le résultat par {a}",
            f"{'Ajouter' if c>0 else 'Retrancher'} {abs(c)} au résultat",
            ]

    remontada=[h(autreantec)]
    remontada+=[remontada[-1]-c]
    remontada+=[remontada[-1]//a]
    remontada+=[remontada[-1]-b]
    descrem=["On part du résultat"]
    descrem+=[f"On {'ajoute' if c<0 else 'retranche'} {abs(c)}"]
    descrem+=[f"On divise par {a}"]
    descrem+=[f"On {'ajoute' if b<0 else 'retranche'} {abs(b)}"]
    
    remontecr = [f"\item {descrem[k]} : {remontada[k]}" for k in range(len(remontada))]
    d["etapes_remontada"]="\n".join(remontecr)    

    etapes_resolution = [f"On part de $h(x)={h(autreantec)}$"]
    etapes_resolution+=[f"C'est à dire ${d['formule']}={h(autreantec)}$"]
    etapes_resolution+=[f"C'est à dire ${a}x={h(autreantec)-(a*b+c)}$ (On {'ajoute' if (a*b+c)<0 else 'retranche'} {abs(a*b+c)} des deux côtés de l'égalité)"]
    etapes_resolution+=[f"C'est à dire $x=\\frac{{{h(autreantec)-(a*b+c)}}}{{{a}}}={autreantec}$ (On divise par {a} des deux côtés de l'égalité)"]
    
    d["etapes_resolution"] = r"\item " + "\n \\item ".join(etapes_resolution)

    return d



def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)