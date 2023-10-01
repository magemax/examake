from template_management import load_template

from random import randint, sample, choice, shuffle

from fractions import Fraction

def to_latex(frac):
    return f"\\frac{{{frac.numerator}}}{{{frac.denominator}}}"

def generer_elements():
    a=randint(1,3)
    a*=choice([-1,1])
    b=randint(1,4)
    if (b*a)>0:
        b*=-1
    Coeffs = (a,b)    
    formules = [(a,b), (0,b), (-a,b),(-a/b,a,Fraction(-a,b)), (a,0)]
    if (a*a!=b):
        formules[1]=(-b/a,b, Fraction(-b,a))
    
    qs=[]
    d={}
    d["formule_1"]=f'{a}x{"+" if b>0 else ""}{b}'
    used=[formules[0]]+sample(formules[1:],3)
    shuffle(used)
    used_used=[i for i in range(len(used)) if used[i]==formules[0]]
    numero_reponse_1 = "ABCD"[min([k for k in range(len(used)) if used[k]==(a,b)])]
    for i in range(4):
        print(i,"ABCD"[i],"ABCD"[i]+"_latex", used)
        d["ABCD"[i]+"_latex"]=f"{used[i][0]:.2f} * x {'+' if used[i][1]>=-0.01 else ''}{used[i][1]:.2f}"
    #Trouver un truc entier quand même faut pas déconner
    restantes=[i for i in range(4) if "ABCD"[i]!=numero_reponse_1]
    shuffle(restantes)
    pots=[]
    for k in range(3):
        print(used[restantes[k]])
        if abs(used[restantes[k]][0]-int(used[restantes[k]][0]+(0.5 if used[restantes[k]][0]>0 else -0.5)))<0.0001 and abs(used[restantes[k]][1]-int(used[restantes[k]][1]+0.5))<0.0001:
            a=int(used[restantes[k]][0]+0.5)
            pots+=[tuple([abs(a)]+list(used[restantes[k]]))]
    
    print(pots)
    pots=sorted(pots, key=lambda k:-k[0])
    a2=int(pots[0][0]+.5)
    b2=int(pots[0][1]+.5)
    
    used_used+=[i for i in range(len(used)) if used[i]==pots[0]]
    instructions=["Penser à un nombre"]

    prod=a2*randint(1, 12/a2)
    fact=prod//a2
    mess=choice([k for k in range(1,9) if abs(k) != abs(b2)])
    if (mess*b2>0):
        mess*=-1
    toadd=(b2+mess)
    if True:
        instructions+=[f"Lui {'ajouter' if toadd>0 else 'soustraire'} {abs(fact*toadd)}"]
        instructions+=[f"Multiplier le résultat par {a2}"]
        instructions+=[f"{'Ajouter' if mess*a2<0 else 'Soustraire'} {abs(mess*a2)} au résultat "]
    instructions+["Dire le nombre obtenu"]
    d["etapes_programme"] = "\\item " +  "\n \\item ".join(instructions)
    print(used)
    d["prog_nombre_entre"]=choice([k for k in range(-4,5) if len([j for j in used if (j[0]-a2)*k+(j[1]-b2)==0])<=1])

    formules3 = []
    kk=1
    for i in range(len(used)):
        if i not in used_used:
            try:
                _,b,a=used[i]
                if a!=int(a):
                    a=to_latex(a)
                else:
                    a=int(a)
            except:
                a,b = used[i]
            if a:
                text=f"{'-' if a<0 else ''}{abs(a) if abs(a)!=1 else''}x{'+' if b>0 else '-' if b<0 else ''}{abs(b) if abs(b) else''}"
            else:
                text=f"{'' if b>0 else '-' if b<0 else ''}{abs(b) if abs(b) else''}"
            formules3+=[f"h_{kk}(x)={text}"]
            kk+=1
    d["formules_3"]= r" \qquad ".join(formules3)
    return d

def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)