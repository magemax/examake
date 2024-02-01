from template_management import load_template

from random import randint, sample, choice
from math import gcd    
from fractions import Fraction

def fraction_to_latex(f):
    if f.denominator ==1:
        return str(f.numerator)
    else:
        return f"\\frac{{{f.numerator}}}{{{f.denominator}}}"

def generer_elements():
    questions=[]
    corrige = []

    #addition même denominateur
    den = randint(5,9)
    num1,num2 = den,den
    while gcd(num1,den)!=1 or gcd(num2,den)!=1:
        num1,num2 = (sample(list(range(1, max(den,den)*2-1)),2))
    f1=Fraction(num1, den)
    f2=Fraction(num2, den)
    fres=f1+f2
    q = f"{fraction_to_latex(f1)} + {fraction_to_latex(f2)}"
    r = f"{fraction_to_latex(f1)} + {fraction_to_latex(f2)} = {fraction_to_latex(fres)}"
    questions += ["$"+q+"$"]
    corrige += ["$"+r+"$"]
    
    #soustraction même denominateur

    den = randint(5,9)
    num1,num2 = den,den
    while gcd(num1,den)!=1 or gcd(num2,den)!=1:
        num1,num2 = (sample(list(range(1, max(den,den)*2-1)),2))
    f1=Fraction(num1, den)
    f2=Fraction(num2, den)
    fres=f1-f2
    q = f"{fraction_to_latex(f1)} - {fraction_to_latex(f2)}"
    r = f"{fraction_to_latex(f1)} - {fraction_to_latex(f2)} = {fraction_to_latex(fres)}"
    questions += ["$"+q+"$"]
    corrige += ["$"+r+"$"]
    
    #multiplication

    den1, den2 = sample(list(range(2,9)),2)
    num1,num2 = (sample(list(range(1, max(den1,den2)*2-1)),2))
    num1,num2 = den1,den2
    while gcd(num1,den1)!=1 or gcd(num2,den2)!=1 or num1*num2%(den1*den2)==0:
        num1,num2 = (sample(list(range(1, max(den1,den2)*2-1)),2))
    f1=Fraction(num1, den1)
    f2=Fraction(num2, den2)
    fres=f1*f2
    q = f"{fraction_to_latex(f1)} \\times {fraction_to_latex(f2)}"
    r = f"{fraction_to_latex(f1)} \\times {fraction_to_latex(f2)} = {fraction_to_latex(fres)}"
    questions += ["$"+q+"$"]
    corrige += ["$"+r+"$"]
    
    #addition

    den1,den2 = 8,8
    while gcd(den1,den2)!=1:
        den1, den2 = sample(list(range(2,9)),2)
    num1,num2 = den1,den2
    while gcd(num1,den1)!=1 or gcd(num2,den2)!=1 :
        num1,num2 = (sample(list(range(1, max(den1,den2)*2-1)),2))
    f1=Fraction(num1, den1)
    f2=Fraction(num2, den2)
    fres=f1+f2
    q = f"{fraction_to_latex(f1)} + {fraction_to_latex(f2)}"
    r = f"{fraction_to_latex(f1)} + {fraction_to_latex(f2)} = {fraction_to_latex(fres)}"
    questions += ["$"+q+"$"]
    corrige += ["$"+r+"$"]
    
    #soustraction

    den1,den2 = 8,8
    while gcd(den1,den2)!=1:
        den1, den2 = sample(list(range(2,9)),2)
    num1,num2 = den1,den2
    while gcd(num1,den1)!=1 or gcd(num2,den2)!=1 :
        num1,num2 = (sample(list(range(1, max(den1,den2)*2-1)),2))
    f1=Fraction(num1, den1)
    f2=Fraction(-num2, den2)
    fres=f1-f2
    q = f"{fraction_to_latex(f1)} - {fraction_to_latex(f2)}"
    r = f"{fraction_to_latex(f1)} - {fraction_to_latex(f2)} = {fraction_to_latex(fres)}"
    questions += ["$"+q+"$"]
    corrige += ["$"+r+"$"]
    

    #division
    den1, den2 = sample(list(range(2,9)),2)
    num1,num2 = den1,den2
    while gcd(num1,den1)!=1 or gcd(num2,den2)!=1 or num1*den2%(den1*num2)==0:
        num1,num2 = (sample(list(range(1, max(den1,den2)*2-1)),2))
    f1= Fraction(num1,den1)
    f2=Fraction(num2,den2)
    fres = f1/f2

    q = f"\\dfrac{{{fraction_to_latex(f1)}}}{{{fraction_to_latex(f2)}}}"
    r = f"\\dfrac{{{fraction_to_latex(f1)}}}{{{fraction_to_latex(f2)}}} = {fraction_to_latex(f1)} \\times \\frac{{{den2}}}{{{num2}}} = {fraction_to_latex(fres)}" #
    questions += ["$"+q+"$"]
    corrige += ["$"+r+"$"]
    
    # addition + produit

    den1, den2, den3 = sample(list(range(2,9)),3)
    num1,num2, num3 = den1,den2, den3
    while gcd(num1,den1)!=1 or gcd(num2,den2)!=1 or gcd(num2,den2)!=1:
        num1,num2, num3 = (sample(list(range(1, max(den1,den2, den3)*2-1)),3))
    f1= Fraction(num1,den1)
    f2=Fraction(num2,den2)
    f3=Fraction(num3,den3)
    fres = f1 + f2 * f3
    q = f"{fraction_to_latex(f1)} + {fraction_to_latex(f2)} \\times {fraction_to_latex(f3)}"
    r = f"{fraction_to_latex(f1)} + {fraction_to_latex(f2)} \\times {fraction_to_latex(f3)} = {fraction_to_latex(fres)}"
    questions += ["$"+q+"$"]
    corrige += ["$"+r+"$"]
    
    listequestions = r"\item" + "\n \\item \n". join(questions)
    listereponses = r"\item" + "\n \\item \n". join(corrige)
    
    return {"questions" : listequestions, "reponses" : listereponses}

def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)