from template_management import load_template

from random import randint, random, sample, choice

from math import pi, sin, cos



def angle_to_direction(angle, size= 2.5):
    x=cos(angle)*size
    y=sin(angle)*size
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

def generer_elements(nbl = 3, nbc = 3):
    pictures=[]
    nombre = nbl * nbc
    cc= "|".join(nbc*"c")
    tableau = [fr"\begin{{tabular}}{{{cc}}} \hline"] 
    for i in range(nombre):
        lettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        rl = sample(lettres, 3)
        dp = dict(zip("ABC", rl))
        a,b,c, aangle2 = angle_random()
        coords={}
        for k in range(3):
            coords["ABC"[k]]=[a,b,c][k]
        contenupicture = []
        for point in "ABC":
            contenupicture+=[fr"\coordinate ({point}) at {coords[point]};"]
        contenupicture+=[fr'\draw pic[draw,fill=blue!30,angle radius=1cm, shift={{(6mm,3mm)}}] {{angle=B--A--C}};']
        for point in "ABC":
            contenupicture+=[f"\\draw plot[mark=x] coordinates{{{coords[point]}}} node[below] {{{dp[point]}}};"]
        for couple in ["BA","AC"]:
            dc = r"\draw "+str(coords[couple[0]])+" -- "+str(coords[couple[1]])+";"
            contenupicture+=[dc]
        nomangle = "".join([dp[k] for k in "BAC"])
        contenupicture=[r"\begin{tabular}{c} \begin{tikzpicture}"]+contenupicture+[r"\end{tikzpicture}","\n"]
        casephoto = "\n".join(contenupicture)

        pictures+=["\n".join(contenupicture)]
        tableau += [fr"{casephoto}" + "\\\\ \n" +fr"\Sicorrection{{$\widehat{{{nomangle}}}={aangle2}^\circ$}}{{$\widehat{{{nomangle}}}= $}} \end{{tabular}}"]
        if i%nbc==nbc-1:
            tableau +=[" \\\\ \\hline \n"]
        else:
            tableau +=" & "
    tableau += [r"\end{tabular}"]
    return {"tableau_triangle" : "\n".join(tableau)}

def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)