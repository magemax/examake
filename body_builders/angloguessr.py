from template_management import load_template

from random import randint, random, sample, choice

from math import pi, sin, cos



def angle_to_direction(angle):
    x=cos(angle)*5
    y=sin(angle)*5
    return (x,y)    

def translate(point, direction, distance):
    return tuple([point[i]+float(distance)*direction[i] for i in range(2)])


def angle_random(): #Renvoie trois points du ABC, tels que l'angle ABC vaille un nombre entier
# de degrés entre 1 et 179
    a=(0,0)
    rangle=random()*pi
    b=angle_to_direction(rangle)
    aangle2=randint(1,179)
    rangle2=pi/180 * aangle2
    c=angle_to_direction(rangle+rangle2)
    return a,b,c, aangle2


def generer_elements(nombre= 6):
    pictures=[]
    for i in range(nombre):
        coords={}
        a,b,c, aangle2 = angle_random()
        for k in range(3):
            coords["ABC"[k]]=[a,b,c][k]
        contenupicture = []
        for point in "ABC":
            contenupicture+=[fr"\coordinate ({point}) at {coords[point]};"]
        contenupicture+=[fr'\draw pic[draw,fill=blue!30,angle radius=1cm, shift={{(6mm,3mm)}}] {{angle=B--A--C}};']
        for point in "ABC":
            contenupicture+=[f"\\draw plot[mark=x] coordinates{{{coords[point]}}} node[below] {{{point}}};"]
        for couple in ["BA","AC"]:
            dc = r"\draw "+str(coords[couple[0]])+" -- "+str(coords[couple[1]])+";"
            contenupicture+=[dc]
        contenupicture=[r"{\centering"]+[r"\begin{tikzpicture}"]+contenupicture+[r"\end{tikzpicture}","\n",
        fr"\Texteouvide{{$\widehat{{BAC}}={aangle2}^\circ$}}", "}"]
        pictures+=["\n".join(contenupicture)]
    return {"content" : "\n \\newpage \n ".join(pictures)}

def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)