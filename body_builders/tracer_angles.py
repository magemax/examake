
from random import randint, random, sample, choice

from math import pi, sin, cos
from cmath import exp
from template_management import load_template

def expa(angle):
    return exp(angle/180*pi * 1j)


class Point:
    def __init__(self, a,b):
        self.c=a+b*1j
    def __str__(self):
        return "("+str(self.c.real) + "," + str(self.c.imag) + ")"


print(expa(90), expa(180))

def make_angle(a,b, angle):
    direction = ((a-b))*expa(angle)
    z=b+direction
    return z.real, z.imag



def angle_to_direction(angle, size= 8):
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

def generer_elements(nbl = 2, nbc = 1):
    
    
    lettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rl = sample(lettres, 4)
    dp = dict(zip("ABCD", rl))
    angle1,angle2=180,180
    while angle1+angle2>=280:
        angle1, angle2 = sample([5*k for k in range(3,34) if k!=18],2)
    a=Point(0,0)
    b=Point(8,randint(0,0))
    c=Point(*make_angle(a.c, b.c, angle1))
    print(a,b,c, angle1)
    d=Point(*make_angle(b.c, a.c, angle2))
    print(a,b,c, angle1)
    coords={}
    for k in range(4):
        coords["ABCD"[k]]=[a,b,c,d][k]

    picture=[r"\begin{tikzpicture}"]
    picturecorrection=[]
    for point in "ABCD":
        picture+=[fr"\coordinate ({point}) at {coords[point]};"]
    for point in "AB":
        picture+=[f"\\draw plot[mark=x] coordinates{{{coords[point]}}} node[below] {{{dp[point]}}};"]
    for point in "CD":
        picture+=[fr"\Sicorrection{{\draw plot[mark=x] coordinates{{{coords[point]}}} node[below] {{{dp[point]}}};}}{{\draw plot[mark=none] coordinates{{{coords[point]}}};}}"]
    for couple in ["BA"]:
        dc = r"\draw "+str(coords[couple[0]])+" -- "+str(coords[couple[1]])+";"
        picture+=[dc]
    for couple in ["AD","BC"]:
        dc = r"\Texteouvide{\draw "+str(coords[couple[0]])+" -- "+str(coords[couple[1]])+";}"
        picture+=[dc]

    picture+=[r"\end{tikzpicture}"]

    questions=[]
    for toput in [("C","A","B", angle1), ("D","B","A", angle2)]:
        questions+=[fr"\item Placer un point ${dp[toput[0]]}$ tel que l'angle $\widehat{{{dp[toput[1]]}{dp[toput[2]]}{dp[toput[0]]}}}$ mesure ${toput[3]}^\circ$, et tracer la demi-droite $[{dp[toput[2]]}{dp[toput[0]]})$."]

    print("\n".join(picture))


    return {"dessin" : "\n".join(picture), "questions" : "\n".join(questions)}





def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)