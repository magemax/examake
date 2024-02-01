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
    global numb
    a,b,c = 10,10,10
    while a+b+c >15 or  a==b:
        a,b,c = sample(list(range(2,10)), 3)
        c=0
    tot=a+b+c

    q = fr"""Dans le frigo, il y a {a+b+c} yaourts. {a} sont à la banane et {b} sont à l'abricot.\\
    Lisa en choisit un au hasard. Son frère Victor en choisit un au hasard à son tour, et on s'intéresse aux yaourts obtenus les deux frères et soeurs.\\
    \textbf {{a.}}  Combien d'issues possède cette experience aléatoire ? Donner un exemple d'issue.\\
    \textbf {{b.}}  Est-ce une expérience en situation d'équiprobabilité ? Justifier.\\
    \textbf {{c.}}  Calculer la probabilité que Lisa et Victor aient choisi tous les deux un yaourt à la banane.\\
    \textbf {{d.}}  Calculer la probabilité qu'ils aient choisi des yaourts aux parfums identiques.\\
    \textbf {{e.}}  Calculer la probabilité qu'ils aient choisi des yaourts aux parfums différents.
    """


    def fraction2epreuvessame(n,N):
        return rf"${fraction_to_latex(Fraction(n,N))} \times {fraction_to_latex(Fraction(n-1,N-1))}=\dfrac{{{n*(n-1)}}}{{{N*(N-1)}}}={fraction_to_latex(Fraction(n*(n-1), N*(N-1)))}$"

    r =  fr"""
    \textbf {{a.}}  Lisa peut avoir choisi un yaourt à la banane ou à l'abricot. Une fois qu'elle a choisi, et comme il y a au moins 2 yaourts de chaque sorte, Victor a les mêmes 2 possibilités. 
    Il y a donc $2\times2=4$ issues possibles.\\
    Par exemple : Lisa a pris un yaourt à la banane et Victor un yaourt à l'abricot. Ce qu'on peut noter (B,A).\\
    Les 9 issues sont : (B,B) (B,A) (A,B) (A,A) .\\
    \textbf {{b.}}  Comme le nombre de yaourts est différent d'un parfum à l'autre, Lisa n'a pas la même probabilité de choisir n'importe quel parfum. On en déduit qu'il est impossible que les issues (B,B), (A,A) et (V,V) aient la même probabilité.\\
    \textbf {{c.}}  Il y a {a} yaourts à la banane, et {tot} yaourts en tout, la probabilité que Lisa choisisse un yaourt à la banane est : ${fraction_to_latex(Fraction(a,tot))}$.\\
    Ensuite, il reste {a-1} yaourts à la banane pour Victor sur un total de {tot-1} yaourts.\\ 
    La probabilité qu'il choisisse à son tour et dans ces conditions ce parfum est : $\dfrac{{{a-1}}}{{{tot-1}}}={fraction_to_latex(Fraction(a-1,tot-1))}$.\\
    La probabilité de l'issue (B,B) est le produit de ces deux probabilités, donc : {fraction2epreuvessame(a,tot)}.\\
    \textbf {{d.}}  Les probabilités de  l'issue (A,A) peuvt être calculée de la même façon qu'à la question c) :\\{fraction2epreuvessame(b,tot)}.\\
    La probabilité qu'ils choisissent le même parfum est la somme des probabilités des issues (B,B) et (A,A), soit :\\
    $\dfrac{{{a*(a-1)}}}{{{tot*(tot-1)}}}+\dfrac{{{b*(b-1)}}}{{{tot*(tot-1)}}}+\dfrac{{{b*(b-1)}}}{{{tot*(tot-1)}}}=\dfrac{a*(a-1) + b*(b-1)}{tot*(tot-1)}={fraction_to_latex(Fraction(a*(a-1) + b*(b-1) , tot*(tot-1)))} $.\\
    \textbf {{e.}}  Choisir des parfums différents est l'événement contraire de l'événement dont on a calculé la probabilité à la question d).\\
    La probabilité de cet événement est donc : $1-{fraction_to_latex(Fraction(a*(a-1) + b*(b-1) + c*(c-1), tot*(tot-1)))}={fraction_to_latex(Fraction(tot*(tot-1) - (a*(a-1) + b*(b-1) + c*(c-1)), tot*(tot-1)))}$
    """

    qs= [q]
    rs= [r]

    primelist = [7, 11, 13, 17, 19]

    a,b,c,d,e,f,g,h = [0]*8
    while a+b+c+d not in primelist:
        a,b,c = [randint(1,6) for i in range(4)]
    while e+f+g+h not in primelist or e+f+g+h == a+b+c+d:
        e,f,g = [randint(1,6) for i in range(4)]

    t1=a+b+c
    t2 = e+f+g

    q = fr"""
    Dans sa commode, Rémi a mis dans le premier tiroir des paires de chaussettes. 
    Il y a {a} paires de chaussettes rouges, {b} paires de chaussettes vertes, {c} paires de chaussettes bleues  \\
    Dans le deuxième tiroir, Rémi a mis des T-shirt. Il y a {e} T-shirt rouges, {f} T-shirt verts et {g} T-shirt noirs\\
    Un matin, il y a une panne de courant et Rémi prend au hasard une paire de chaussettes dans le premier tiroir et un T-shirt dans le deuxième.\\
    \textbf {{a.}} Quelle est la probabilité que Rémi ait choisi un T-shirt noir ?\\
    \textbf {{b.}} Quelle est la probabilité que Rémi ait choisi des chaussettes rouges et un T-shirt rouges ?\\
    \textbf {{c.}}  Quelle est la probabilité que Rémi ait choisi des chaussettes et un T-shirt de la même couleur ?\\
    \textbf {{d.}}  Quelle est la probabilité que Rémi ait choisi des chaussettes et un T-shirt de couleurs différentes ?
    """

    def compose(c,g,t1,t2):
        return fr"{fraction_to_latex(Fraction(c, t1))}\times {fraction_to_latex(Fraction(g,t2))}={fraction_to_latex(Fraction(c*g, t1*t2))}"

    r = fr"""
    \textbf {{a.}} Il y a {g} T-shirt rouges, sur {t2} T-shirts possibles. Comme Rémi fait son choix au hasard, les {t2} t-shirts sont équiprobables. La probabilité de choisir un t-shirt rouge est donc ${fraction_to_latex(Fraction(g,t2))}$
    \textbf {{b.}}  Il y a {a} paires de chaussettes rouges et il y a {t1} paires de chaussettes possibles.
    La probabilité de choisir une paire de chaussettes blanches est : ${fraction_to_latex(Fraction(a, t1))}$.\\
    Il y a {e} T-shirt rouges sur {t2} T-shirt possibles. La probabilité de choisir un des T-shirt bleu est : 
    ${fraction_to_latex(Fraction(g,t2))}$.\\
    Jean-Claude a donc une probabilité de ${compose(a,e,t1,t2)}$ de choisir un t-shirt rouge et des chaussettes rouges.\\
    
    \textbf {{c.}}  La probabilité de choisir une paire de chaussettes vertes est : ${fraction_to_latex(Fraction(b, t1))}$ et la probabilité de choisir l'un des T-shirt verts est : ${fraction_to_latex(Fraction(f, t2))}$.\\
    Donc la probabilité de choisir des chaussettes et un T-shirt verts est : ${compose(b,f,t1,t2)}$.\\
    On en déduit que la probabilité de choisir des chaussettes et un T-shirt de la même couleur est :\\${fraction_to_latex(Fraction(b*f, t1*t2))} + {fraction_to_latex(Fraction(a*e, t1*t2))}  = {fraction_to_latex(Fraction( b*f + a*e , t1*t2))}$.\\
    \textbf {{d.}}  L'événement "choisir des chaussettes et un T-shirt de couleurs différentes" est l'événement contraire de l'événement "choisir des chaussettes et un T-shirt de même couleur".\\
    Donc sa probabilité est : $1-{fraction_to_latex(Fraction( b*f + a*e, t1*t2))}={fraction_to_latex(Fraction(t1*t2 - (b*f + a*e), t1*t2))}$.\\ 
    """

    qs+=[q]
    rs+=[r]



    d={}
    whom=numb
    numb=1-numb
    d["question"] = qs[whom]
    d["full_corrige"] = rs[whom]
    return d


def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)