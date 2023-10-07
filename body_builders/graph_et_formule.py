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
    a=randint(1,3)
    a*=choice([-1,1])
    b=randint(1,4)
    if (b*a)>0:
        b*=-1
    Coeffs = (a,b)    
    formules = [(a,b), (0,b), (-a,b),((-a/b,a,Fraction(-a,b)) if a%b else (-a//b,a)), (a,0)]
    if (a*a!=b):
        formules[1]=(-b/a,b, Fraction(-b,a))
    
    qs=[]
    d={}
    d["formule_1"]=affine_to_latex(a,b)
    #Une autre fonction 
    aa, bb= a,b
    while (a,b)==(aa,bb):
        aa=choice([-1,1])*randint(2,3)
        bb=randint(1,4)

    used=[formules[0]]+[(aa,bb)]+sample(list(set([f for f in formules[1:] if f!=(aa,bb)])),2)
    shuffle(used)

    used_used=[i for i in range(len(used)) if used[i]==formules[0]]
    numero_reponse_1 = "ABCD"[min([k for k in range(len(used)) if used[k]==(a,b)])]
    d["rep_1"]=numero_reponse_1
    d["f0"]=b
    if abs(b+a)<=4:
        d["autreval"]=1
        d["fav"]=b+a
    else:
        d["autreval"]=-1
        d["fav"]=b-a
        
    numero_reponse_2 = "ABCD"[min([k for k in range(len(used)) if used[k]==(aa,bb)])]
    d["rep_2"]=numero_reponse_2
    #Trouver un truc entier quand même faut pas déconner
    #Bon finalement je dois générer une fonction au hasard qui :
    # - soit genre ax+b
    # - avec 2<=abs(a)<=3
    # - avec 1<=abs(b)<=4
    # - ne soit pas la fonction choisie en 1
    for i in range(4):
        print(i,"ABCD"[i],"ABCD"[i]+"_latex", used)
        d["ABCD"[i]+"_latex"]=f"{used[i][0]:.2f} * x {'+' if used[i][1]>=-0.01 else ''}{used[i][1]:.2f}"


    used_used+=[i for i in range(len(used)) if used[i]==(aa,bb)]
    instructions=["Penser à un nombre"]
    # aa x + bb
    # aa *(x + fact ) + bb-(fact * aa)
    prod=aa*randint(1, 12//abs(aa))
    fact=prod//aa
    toadd=(bb-prod)
    formx="x"
    if True:
        instructions+=[f"Lui {'ajouter' if fact>0 else 'soustraire'} {abs(fact)}"]
        formx=f"({formx}{'+' if fact>=0 else ''}{fact})"
        instructions+=[f"Multiplier le résultat par {aa}"]
        formx=f"({aa} \\times {formx})"
        instructions+=[f"{'Ajouter' if prod-bb<0 else 'Soustraire'} {abs(prod-bb)} au résultat "]
        formx=f"({formx}{'+' if bb-prod>=0 else ''}{bb-prod})"
    
    instructions+["Dire le nombre obtenu"]
    d["etapes_programme"] = "\\item " +  "\n \\item ".join(instructions)
    print(used)
    d["prog_nombre_entre"]=choice([k for k in range(-4,5) if len([j for j in used if (j[0]-aa)*k+(j[1]-aa)==0])<=1])
    d["prog_from_a"]=formx.replace("x",str(d["prog_nombre_entre"]))
    d["g_a"]=d["prog_nombre_entre"]*aa+bb
    d["formulecalc"]=f"$g(x)={formx}={affine_to_latex(aa, prod)}{'+' if toadd>=0 else ''}{toadd}={affine_to_latex(aa,bb)}$"
    formules3 = []
    kk=1
    for i in range(len(used)):
        if i not in used_used:
            try:
                _,b,a=used[i]
            except:
                a,b = used[i]
            if a:
                if a!=int(a):
                    a_text=to_latex(a)
                else:
                    a_text=f"{'-' if a<0 else ''}{abs(a) if abs(a)!=1 else''}"
                text=f"{a_text}x{'+' if b>0 else '-' if b<0 else ''}{abs(b) if abs(b) else''}"
            else:
                text=f"{'' if b>0 else '-' if b<0 else ''}{abs(b) if abs(b) else''}"
            formules3+=[f"{text}"]
            kk+=1
    unused= sample([k for k in formules if k not in used],2)

    for i in range(len(unused)):
        if i not in used_used:
            try:
                _,b,a=unused[i]
            except:
                a,b = unused[i]
            if a:
                if a!=int(a):
                    a_text=to_latex(a)
                else:
                    a_text=f"{'-' if a<0 else ''}{abs(a) if abs(a)!=1 else''}"
                text=f"{a_text}x{'+' if b>0 else '-' if b<0 else ''}{abs(b) if abs(b) else''}"
            else:
                text=f"{'' if b>0 else '-' if b<0 else ''}{abs(b) if abs(b) else''}"
            formules3+=[f"{text}"]
            kk+=1
    shuffle(formules3)

    #Troisième boucle pour dire quel élément de formules3 correspond à quel graphique utilisé

    corresp=[]
    for i in range(len(used)):
        if i not in used_used:
            try:
                _,b,a=used[i]
            except:
                a,b = used[i]
            if a:
                if a!=int(a):
                    a_text=to_latex(a)
                else:
                    a_text=f"{'-' if a<0 else ''}{abs(a) if abs(a)!=1 else ''}"
                text=f"{a_text}x{'+' if b>0 else '-' if b<0 else ''}{abs(b) if abs(b) else''}"
            else:
                text=f"{'' if b>0 else '-' if b<0 else ''}{abs(b) if abs(b) else''}"
            for j in range(len(formules3)):
                if text==formules3[j]:
                    corresp+=[("ABCD"[i],f"$h_{j+1}$")]
    d["reponse_4"]=" \n \\item ".join([""] + [k[1]+' correspond à la courbe ' + k[0] for k in corresp])
    formules3=[f"h_{k+1}(x)="+formules3[k] for k in range(len(formules3))]
    d["formules_3"]= r" \qquad ".join(formules3)
    return d

def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)