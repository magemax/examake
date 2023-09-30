from template_management import load_template

from random import randint, sample 
from scipy.interpolate import lagrange
import numpy as np
from numpy.polynomial.polynomial import Polynomial
import matplotlib.pyplot as plt

# Plein de fonctions auxiliaires trop relou parce que c'est du legacy

def Randomvalues(liste_antecedents, valeur_min, valeur_max):
    return [randint(valeur_min,valeur_max) for _ in liste_antecedents]


def gen_random_xy(valmin=-7, valmax=7, nb_points_interm=5, maximage=7, minimage=-2, buffer=1, show=True):
    nbgen=0
    while True:
        tbase=[valmin,valmax]
        Autresvalues = sample(list(range(valmin+1,valmax)),nb_points_interm)
        tbase=sorted(tbase+Autresvalues)
        nbgen+=1
        values=Randomvalues(tbase,minimage+buffer, maximage-buffer)
        x = np.array(tbase)
        y= np.array(values)
        poly = lagrange(x,y)
       # print(Polynomial(poly.coef[::-1]).coef)
        delta = 0
        epsilon = 0.01
        dt = 0.1
        x_new = np.arange(valmin-delta, valmax+delta + epsilon, dt)
        y_new=Polynomial(poly.coef[::-1])(x_new)
        #print(values, max(abs(y_new)))
        if max(y_new)<=maximage and min(y_new)>=minimage:
            break
    if show==True:
        plt.scatter(x, y, label='data')
        plt.plot(x_new, y_new, label='Polynomial')
        plt.legend()
        plt.show()
    return {"x":x_new, "y":y_new,"x_key":tbase, "y_key":values, "nb_tries":nbgen}

def dict_to_graph(d):
    Textcoords=[f"({d['x'][k]:.5f},{d['y'][k]:.6f})" for k in range(len(d["x"]))]
    return("\n".join(Textcoords))

def dict_to_graph2(d):
    Textcoords=[f"({d['antecedents'][k]:.5f},{d['images'][k]:.6f})" for k in range(len(d["antecedents"]))]
    return("\n".join(Textcoords))


def dict_to_stuff(d):
    #Liste des points pour le TDV :
    indices_points=sorted(sample(list(range(len(d["x_key"]))), 4))
    autres_indices=[k for k in range(len(d["x_key"])) if k not in indices_points]
    autres_indices=sample(autres_indices, len(autres_indices))
    print(indices_points, autres_indices)
    text=" & ".join([f"${str(d['x_key'][_])}$" for _ in indices_points])

    #texte des images
    images_cachees=" & ".join([" " for _ in indices_points])
    images= " & ".join([f"${str(d['y_key'][_])}$" for _ in indices_points])
    ycoords = r"\Sicorrection{" +images+"}{"+images_cachees+"}"
    return {"champ_tdval":text, "ycoords":ycoords,"autres":[(d["x_key"][_],d["y_key"][_]) for _ in autres_indices]}

def valeurs_y(antecs,y_0,y_1): 
    #Renvoie un tableau qui commence à y_0, finit à y_1, est censé commencer et finir à 0 de dérivée, est de signe constant
    #Et a le même nombre d'éléments que antecs
    tablovars=[i*(len(antecs)-i) for i in range(len(antecs))]
    tablovars=[(y_1-y_0)*k/sum(tablovars) for k in tablovars]
    res=[y_0]
    for i in range(1,len(antecs)):
        res+=[res[-1]+tablovars[i]]
    return res

def list_to_random(keys):
    qs=[r"\item L'image de $xx$ par la fonction $f$ est $yyh$"]
    qs+=[r"\item Un antécédent de $yy$ par la fonction $f$ est $xxh$"]
    qs+=[r"\item Le nombre $yy$ admet exactement \dots antécédent(s) par la fonction f"]
    qs+=[r"\item $f(xx)=yyh$"]
    qs+=[r"\item $f(xxh)=yy$"]
    questionsused=sample(qs, len(keys))
    for k in range(len(keys)):
        trxxh= "\\Texteoulongueur{"+str(keys[k][0])+"}{0.7}"
        tryyh= "\\Texteoulongueur{"+str(keys[k][1])+"}{0.7}"
        questionsused[k]=questionsused[k].replace("xxh",trxxh).replace("yyh",tryyh)
        questionsused[k]=questionsused[k].replace("xx",str(keys[k][0])).replace("yy",str(keys[k][1]))
        
    return "\n".join(questionsused)


def random_tablo_variation():
    try:
        #Choisir début et fin de l'intervalle
        debut_interv,fin_interv=0,0
        while debut_interv-fin_interv>=-10 or fin_interv-debut_interv>=15:
            debut_interv,fin_interv=randint(-10,-1), randint(1,10)
        nb_zones=randint(3,4)
        extremas=sorted(sample(list(range(debut_interv+1,fin_interv)), nb_zones-1))
        value12=sample(list(range(-3,3)),2)
        if value12[0]>value12[1]:
            sens=[-1]
        else:
            sens=[1]
        for i in range(nb_zones-1):
            sens+=[sens[-1]*-1]
            if sens[-1]>0:
                newvalue=randint(value12[-1]+1,max(3, value12[-1]+1))
            else:
                newvalue=randint(min(-3,value12[-1]-1),value12[-1]-1)
            value12+=[newvalue]
        antecs=[debut_interv]+extremas+[fin_interv]
        images=value12
        #Nice ça a l'air de marcher. Maintenant je fais des samples
        dx=0.1
        fullantecs=np.arange(antecs[0],antecs[-1]+dx/2, dx)
        rimgs=[value12[0]]
        for i in range(len(antecs)-1):
            rantecs=np.arange(antecs[i],antecs[i+1]+dx/2, dx)
            rimgs+=valeurs_y(rantecs, value12[i],value12[i+1])[1:]
        dr={}
        dr["fake_antecs"]=antecs
        dr["fake_imgs"]=value12
        dr["antecedents"]=fullantecs
        dr["images"]=rimgs
        dr["min_y"]=int(min(value12)-0.01)
        dr["max_y"]=int(max(value12)+0.01)
        dr["min_x"]=debut_interv
        dr["max_x"]=fin_interv
        return dr
    except:
        raise
        return None



#Fonction qui se démerde pour renvoyer 

def build(**args): 
    print(args)
    texte_individuel=load_template(args["template"])
    dico_random=gen_random_xy(show=False)

    d2=dict_to_stuff(dico_random)
    dico3=random_tablo_variation()
    while dico3["min_y"]<-3 or dico3["max_y"]>3 or dico3["max_y"]*dico3["min_y"]>=0:
        dico3=random_tablo_variation()
    for k,v in dico3.items():
        print(k,v)
    print(f"Generated rand values. {dico_random['nb_tries']}")
    

    a_inserer=texte_individuel
    a_inserer=a_inserer.replace("{w_coords}",dict_to_graph(dico_random))
    a_inserer=a_inserer.replace("{w_xcoords}",d2["champ_tdval"])
    a_inserer=a_inserer.replace("{w_ycoords}",d2["ycoords"])
    a_inserer=a_inserer.replace("{w_randomquestions}",list_to_random(d2["autres"]))
    a_inserer=a_inserer.replace("{w_xmin}",str(dico3["min_x"]))
    a_inserer=a_inserer.replace("{w_xmax}",str(dico3["max_x"]))
    a_inserer=a_inserer.replace("{w_ymin}",str(-3))
    a_inserer=a_inserer.replace("{w_ymax}",str(3))
    a_inserer=a_inserer.replace("{w_coords2}",dict_to_graph2(dico3))
    print(len(a_inserer))
    return(a_inserer)