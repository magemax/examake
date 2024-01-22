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
    ld=["OA","OB"]
    #Attention, cotes est ptet neg.
    cotes=sample([6,12],2)
    scale= (8+random()) / float(max([abs(i) for i in cotes]))
    dists=dict(zip(ld, cotes))
    
    picture_elements=[]
    picture_elements_corrige=[]

    pc={}
    #Check la taille initiale sans scale
    pc["O"] = point_intersection
    diram= angle_to_direction(angle_1)
    pc["A"] = translate(pc["O"], diram, float(dists["OA"]))
    dirbn=angle_to_direction(angle_2)
    pc["B"] = translate(pc["O"], dirbn, float(dists["OB"]))

    hauteur = max([v[0] for v in pc.values()])-min([v[0] for v in pc.values()])
    largeur = max([v[1] for v in pc.values()])-min([v[1] for v in pc.values()])
    
    scale= min( (8+random()) / hauteur, (8 + random()) / largeur)


    coords={}
    
    #directions et points
    coords["O"] = point_intersection
    diram= angle_to_direction(angle_1)
    coords["A"] = translate(coords["O"], diram, float(dists["OA"])*scale)
    dirbn=angle_to_direction(angle_2)
    coords["B"] = translate(coords["O"], dirbn, float(dists["OB"])*scale)

    names=sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ",3)
    
    dnames=dict(zip("OAB",names))


    #placement des noms de points:
    node_placement={}
    node_placement["O"]=wherenodefromangle([angle_1, angle_2])
    node_placement["A"]=wherenodefromangle([angle_1])
    node_placement["B"]=wherenodefromangle([angle_2])

    for point in "OAB":
        picture_elements+=[f"\\draw plot[mark=x] coordinates{{{coords[point]}}} node[{node_placement[point]}] {{{dnames[point]}}};"]


    #segments
    dab = r"\draw "+str(coords["A"])+" -- "+str(coords["B"])+";"
    picture_elements_corrige+=[dab]
    doa = r"\draw "+str(coords["A"])+" -- "+str(coords["O"])+";"
    picture_elements_corrige+=[doa]
    dob = r"\draw "+str(coords["O"])+" -- "+str(coords["B"])+";"
    picture_elements_corrige+=[dob]

    for segs in ["AB","OA","OB"]:
        c1=coords[segs[0]]
        c2=coords[segs[1]]
        mid=((c1[0]+c2[0])/2,(c1[1]+c2[1])/2)
        direction=(c2[0]-c1[0],c2[1]-c1[1])
        dorth=(direction[1], - direction[0])
        normorth=(dorth[0]**2+dorth[1]**2)**.5
        dorth = (dorth[0]*5/normorth, dorth[1]*5/normorth)
        med1=(mid[0]+dorth[0], mid[1]+dorth[1])
        med2=(mid[0]-dorth[0], mid[1]-dorth[1])
        mediatrice = r"\draw "+str(med1)+" -- "+str(med2)+";"
        picture_elements_corrige+=[mediatrice]
    

    d["picture_sujet"]="\n".join(picture_elements)
    d["picture_correction"]="\n".join(picture_elements + picture_elements_corrige)
    d["questions"]="\n".join([f"\item Sur ce dessin, tracer les segments $[{dnames['O']}{dnames['A']}]$, $[{dnames['O']}{dnames['B']}]$ et $[{dnames['B']}{dnames['A']}]$",
                            f"\item Tracer la médiatrice de chacun des trois segments."])

    return d

def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)

if __name__ == '__main__':
    print(generer_elements()["picture_content"])