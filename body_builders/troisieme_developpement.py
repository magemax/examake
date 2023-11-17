from template_management import load_template
from random import randint, shuffle, choice


class Expression:
    def __init__(self, question, corrige) -> None:
        self.question=question
        self.corrige= corrige


exprs=[]

exprs+=[Expression(r"-(4c+3) + (-2c+1)", r"-(4c+3) + (-2c+1)$= -4c-3  -2c+1$=-6c-2")]
exprs+=[Expression(r"(-4b-4) - (10b^2+9b-1)", r"(-4b-4) - (10b^2+9b-1)= -4b-4  -10b^2-9b+1=-10b^2-13b-3")]
exprs+=[Expression(r"(9c^2+5c-4) - (3c^2-4c-1)", r"(9c^2+5c-4) - (3c^2-4c-1)= 9c^2+5c-4  -3c^2+4c+1=6c^2+9c-3")]
exprs+=[Expression(r"-(8y+4) + (-y^2+3y+4)", r"-(8y+4) + (-y^2+3y+4)= -8y-4  -y^2+3y+4=-y^2-5y")]
exprs+=[Expression(r"-(-7z^2-6z+10) + (-10z^2+7z+3)", r"-(-7z^2-6z+10) + (-10z^2+7z+3)= 7z^2+6z-10  -10z^2+7z+3=-3z^2+13z-7")]
exprs+=[Expression(r"(2x+6) - (10x+3)", r"(2x+6) - (10x+3)= 2x+6  -10x-3=-8x+3")]

Q1 = exprs[:]


exprs=[]
exprs+=[Expression(r"(4z-3)\times 10z", r"10z\times 4z+10z\times(-3)=40z^2-30z")]
exprs+=[Expression(r"2(-4b-7)", r"2\times (-4b)+2\times(-7)=-8b-14")]
exprs+=[Expression(r"(-3y-2)\times(-10)", r"-10\times (-3y)+(-10)\times(-2)=30y+20")]
exprs+=[Expression(r"-10x(-3x+6)", r"-10x\times (-3x) + (-10x)\times 6=30x^2-60x")]
exprs+=[Expression(r"10(2x-9)", r"10\times 2x+10\times(-9)=20x-90")]
exprs+=[Expression(r"(2x+6)\times(-7)", r"-7\times 2x+(-7)\times6=-14x-42")]

Q2= exprs[:]

exprs=[]

exprs+=[Expression(r"(x+2)(x+12)", r"(x+2)(x+12)= x^2+2x+12x+24= x^2+14x+24")]
exprs+=[Expression(r"(2x+4)(5x+9)", r"(2x+4)(5x+9)= 10x^2+18x+20x+36= 10x^2+38x+36")]
exprs+=[Expression(r"(x+4)(x+5)", r"(x+4)(x+5)= x^2+4x+5x+20= x^2+9x+20")]
exprs+=[Expression(r"(8x+5)(2x+7)", r"(8x+5)(2x+7)= 16x^2+56x+10x+35= 16x^2+66x+35")]
exprs+=[Expression(r"(x+10)(x+5)", r"(x+10)(x+5)= x^2+10x+5x+50= x^2+15x+50")]

Q3= exprs[:]


exprs=[]


exprs+=[Expression(r"-x+(10x-11)(8x-3)", r"-x+(10x-11)(8x-3)=-x+80x^2-30x-88x+33=80x^2-119x+33")]
exprs+=[Expression(r"7+(8x-3)(x-10)", r"7+(8x-3)(x-10)=7+8x^2-80x-3x+30=8x^2-83x+37")]
exprs+=[Expression(r"(x\times2)(9x+9)", r"(x\times2)(9x+9)=2x\times(9x+9)=18x^2+18x")]
exprs+=[Expression(r"11-(-2x+5)(6x+10)", r"11-(-2x+5)(6x+10)=11-(-12x^2-20x+30x+50)=11+12x^2+20x-30x-50=12x^2-10x-39")]
exprs+=[Expression(r"3(5x-9)-(-3-9x)", r"3(5x-9)-(-3-9x)=15x-27-(-3-9x)=15x-27+3+9x=24x-24")]

Q4 = exprs[:]

exprs=[]
exprs+=[Expression(r"(4x-8)(4x+8)", r"(4x-8)(4x+8)= (4x)^2-8^2= 16x^2-64")]
exprs+=[Expression(r"(9c-7)(9c+7)", r"(9c-7)(9c+7)= (9c)^2-7^2= 81c^2-49")]
exprs+=[Expression(r"(8x-6)(8x+6)", r"(8x-6)(8x+6)= (8x)^2-6^2= 64x^2-36")]
exprs+=[Expression(r"(4z-6)(4z+6)", r"(4z-6)(4z+6)= (4z)^2-6^2= 16z^2-36")]
exprs+=[Expression(r"(7z-9)(7z+9)", r"(7z-9)(7z+9)= (7z)^2-9^2= 49z^2-81")]

Q5 = exprs[:]



exprs=[]
exprs+=[Expression(r"(5c+9)^2",r"(5c+9)^2=(5c+9)(5c+9)= 5c \times 5c + 5c \times 9 + 9 \times 5c  + 9 \times 9=25c^2+45c+45c+81=25c^2+90c+81")]
exprs+=[Expression(r"(2+3a)^2",r"(2+3a)^2=(2+3a)(2+3a)= 2 \times 2 +  2 \times 3a +  3a \times 2  + 3a \times 3a =4+6a+6a+9a^2=9a^2+12a+4")]
exprs+=[Expression(r"(6y-2)^2",r"(6y-2)^2=(6y-2)(6y-2)= 6y \times 6y + 6y \times (-2) + (-2) \times 6y  + (-2) \times (-2)=36y^2-12y-12y+4=36y^2-24y+4")]
exprs+=[Expression(r"(2-4z)^2",r"(2-4z)^2=(2-4z)(2-4z)= 2 \times 2 +  2 \times (-4z) +  (-4z) \times 2  + (-4z) \times (-4z) =4-8z-8z+16z^2=16z^2-16z+4")]

Q6 = exprs[:]


lettres="ABCDEFGHIJKL"

def generer_elements():
    xtouse=[]
    for choosefrom in [Q1,Q2,Q3, Q4, Q5, Q6]:
        xtouse+=[choice(choosefrom)]

    #shuffle
    shuffle(xtouse)
    d={}
    d["questions"] =r"\item "+ f"\n \\item ".join(["$"+lettres[k]+"="+ xtouse[k].question+"$" for k in range(len(xtouse))])
    d["corriges"] = r"\item "+f"\n \\item ".join(["$"+lettres[k]+"="+ xtouse[k].corrige+"$" for k in range(len(xtouse))])
    d["enonce"]=r"Développer et réduire les expressions suivantes"
    return d



def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)