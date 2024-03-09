from template_management import load_template

from random import randint, sample, choice, shuffle

from fractions import Fraction

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
    
    isok=False
    while not isok:
        a,c=sample([1,2,3,4],2)
        a*=choice([-1,1])
        b=randint(1,7)
        if (b*a)>0:
            b*=-1
        Coeffs = (a,b)
        if a>0:
            c=-c
        dd=randint(-8,8)

        if max(abs(a*(dd-b)/(a-c)+b), abs((dd-b)/(a-c)))<8 and a+b !=c+dd:
            isok=True

    #ax+b=cx+d <=> x = (d-b)/(a-c)    alors   a*(d-b)/(a-c) + b

    formules = [(a,b), (c,dd)]
    
    croisement = ((dd-b)/(a-c), a*(dd-b)/(a-c) + b)


    d={}
    d["formule_1"]=affine_to_latex(a,b)
    d["f_latex"] = f"{a} * x + {b}"
    d["formule_g"]=affine_to_latex(c,dd)
    d["g_latex"] = f"{c} * x + {dd}"

    d["rep1a"] = fr"On remarque que les points (0,{b}) et (1,{a+b}) sont sont la droite (d). On a donc $f(0) = {b}$ et $f(1)= {a+b}$. Le coefficient directeur est donné par la différence entre les deux images. Il est donc de ${a+b}-{b if b > 0 else '('+str(b)+')'}={a}$."
    d["rep1b"] = fr"L'ordonnée à l'origine est l'ordonnée du point où (d) croise l'axe des ordonnées. C'est à dire ${b}$ puisque le point $(0,{b})$ est sur la droite $(d)$"
    d["rep1c"] = fr"On déduit des deux premières questions la formule de $f$ : $f(x) = {affine_to_latex(a,b)}$"

    d["rep2a"] = fr"On calcule : $g(0)={dd}$, et $g(1)={c+dd}$."
    d["rep2b"] = fr"D'après la question précédente, les points $(0,{dd})$ et $(1,{c+dd})$ sont sur la droite (e) qui représente la fonction $g$. On place ces deux points sur le repère et on trace la droite $g$."
    d["rep2c"] = fr"Sur le dessin, les deux droites (d) et (e) semblent se croiser à un point ayant une abscisse d'environ {str(croisement[0]).replace('.',r'{,}')}. C'est donc une valeur approchée du nombre qui a la même image par les fonctions $f$ et $g$"
    return d

def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)