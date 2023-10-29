from template_management import load_template

from random import random, choice, sample
from math import pi , cos, sin
from fractions import Fraction
from decimal import Decimal

def angle_to_direction(angle):
    x=cos(angle)
    y=sin(angle)
    return (x,y)    

def translate(point, direction, distance):
    return tuple([point[i]+float(distance)*direction[i] for i in range(2)])

def dec_to_latex(d):
    return str(d).replace(".","{,}")

def wherenodefromangle(angles):
    if len([x for x in angles if pi/3<=x<=2*pi/3])==0:
        return "below"
    if len([x for x in angles if (x<pi/6 or x>3*pi/6)])==0:
        return "left"
    return "below left"
    


def generer_elements(typ=0): #typ=0 pour direct, sinon 1
    d={}
    point_intersection=(0,0)
    angle_1=random()*pi
    angle_2=(angle_1+(pi/6) + random()*(pi-pi/3))%pi
    #ratio = ratio entre côtés de base et côtés inconnus
    #ratio2 = ratio entre côté connu et coté inconnu
    #Si le produit deux ratios est de 
    ratio=1
    ratio2=1
    while ratio*ratio2%10 and ratio*ratio2%100!=0:
        ratio=Decimal(choice([_ for _ in range(6,20) if _!=10]))
        ratio2=Decimal(choice([-1,1])*choice([_ for _ in range(5,26) if _!=10]))
    
    distbase=Decimal(choice([k for k in range(2,19) if k != 10]))
    ratio/=10
    ratio2/=10
    ld=["OA","OB","OM","ON"]
    #Attention, cotes est ptet neg.
    cotes=[distbase,distbase*ratio, distbase*ratio2, distbase*ratio*ratio2]
    cotes=[k.normalize() if (k%10)!=0 else (k+Decimal(1)).normalize()-1 for k in cotes]
    scale= (8+random()) / float(max([abs(i) for i in cotes]))
    dists=dict(zip(ld, cotes))
    
    picture_elements=[]

    coords={}
    


    #directions et points
    coords["O"] = point_intersection
    diram= angle_to_direction(angle_1)
    coords["A"] = translate(coords["O"], diram, float(dists["OA"])*scale)
    coords["M"] = translate(coords["O"], diram, float(dists["OM"])*scale)
    dirbn=angle_to_direction(angle_2)
    coords["B"] = translate(coords["O"], dirbn, float(dists["OB"])*scale)
    coords["N"] = translate(coords["O"], dirbn, float(dists["ON"])*scale)

    names=sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ",5)
    
    dnames=dict(zip("OAMBN",names))
    for name in ld+["AB","MN", "AM","BN"]:
        dnames[name]=dnames[name[0]]+dnames[name[1]]

    #Distances 
    distancestext=[]
    for k in ld[:-1]:
        distancestext+=[f"{dnames[k]} = {dec_to_latex(abs(dists[k]))} cm"]

    donnees_dists = " ; ".join(distancestext) 

    question=f"Calculer la longueur {dnames[ld[-1]]}"
    


    #placement des noms de points:
    node_placement={}
    node_placement["O"]=wherenodefromangle([angle_1, angle_2])
    node_placement["A"]=wherenodefromangle([angle_1])
    node_placement["M"]=wherenodefromangle([angle_1])
    node_placement["B"]=wherenodefromangle([angle_2])
    node_placement["N"]=wherenodefromangle([angle_2])

    for point in "OAMBN":
        picture_elements+=[f"\\draw {coords[point]} node[{node_placement[point]}] {{{dnames[point]}}};"]


    #Droite AM
    pam=sorted([coords[k] for k in "OAM" ])
    newpoints=[translate(pam[0], diram, -1*scale),translate(pam[0], diram, 1*scale),translate(pam[-1], diram, 1*scale),translate(pam[-1], diram, -1*scale)]
    pam=[min(newpoints)] +pam + [max(newpoints)]
    dam = r"\draw "+str(pam[0])+" -- "+str(pam[-1])+";"
    picture_elements+=[dam]    
    
    #Droite BN
    pbn=sorted([coords[k] for k in "OBN"])
    newpoints=[translate(pbn[0], dirbn, -1*scale),translate(pbn[0], dirbn, 1*scale),translate(pbn[-1], dirbn, 1*scale),translate(pbn[-1], dirbn, -1*scale)]
    pbn=[min(newpoints)] +pbn  + [max(newpoints)]
    dbn = r"\draw "+str(pbn[0])+" -- "+str(pbn[-1])+";"
    picture_elements+=[dbn]    
    print(pbn, pam, sep="\n")

    #AB
    dab = r"\draw [dashed]"+str(coords["A"])+" -- "+str(coords["B"])+";"
    picture_elements+=[dab]
    

    #NM
    dnm = r"\draw [dashed]"+str(coords["N"])+" -- "+str(coords["M"])+";"
    picture_elements+=[dnm]

    print(angle_1, angle_2)
    d["distances_donnees"] = donnees_dists
    d["picture_content"]="\n".join(picture_elements)
    d["question"] = question

    corrtable = []
    print(dnames)
    corrtable+=[f"Les droites ({dnames['AM']}) et ({dnames['BN']}) sont sécantes en {dnames['O']}."]
    corrtable+=[f"Les droites ({dnames['AB']}) et ({dnames['MN']}) sont parallèles."]
    corrtable+=[f"D'après le théorème de Thalès, l'égalité  $\\frac{{{dnames['ON']}}}{{{dnames['OB']}}}=\\frac{{{dnames['OM']}}}{{{dnames['OA']}}}$ est donc vraie."]
    corrtable+=[f"En remplaçant par leur valeurs les longueurs connues, on obtient  $\\frac{{{dnames['ON']}}}{{{dec_to_latex(abs(dists['OB']))}}}=\\frac{{{dec_to_latex(abs(dists['OM']))}}}{{{dec_to_latex(abs(dists['OA']))}}}$."]
    corrtable+=[f"On en déduit ${dnames['ON']}=\\frac{{{dec_to_latex(abs(dists['OB']))} \\times {dec_to_latex(abs(dists['OM']))}}}{{{dec_to_latex(abs(dists['OA']))}}}={dec_to_latex(abs(dists['ON']))}$"]
    corrtable+=[f"La longueur du segment [{dnames['ON']}] est donc de {dec_to_latex(abs(dists['ON']))} centimètres."]
    d["full_corrige"] = "\n\n".join(corrtable)    
    d["predistances_donnees"]="""Dans le dessin suivant, les droites représentées en pointillés sont parallèles.

    On donne les mesures suivantes : """
    return d

def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)

if __name__ == '__main__':
    print(generer_elements()["picture_content"])