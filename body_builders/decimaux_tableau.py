
from random import randint, sample, choice, shuffle


tabunites= ["unité", "dixième", "centième", "millième", "dix-millième"]

class wdec:
    def __init__(self, descstr):
        if "." not in descstr:
            descstr+=".0"
        pe,pd= map(int, descstr.split("."))
        self.pe = pe  #partie entiere
        self.pd = pd  # partie décimale (format entier)
        self.ld = len(descstr.split(".")[1])
        self.ud = 10**self.ld    # dénominateur decimal
    def lecture(self):
        partiedec = f"et {self.pd} {tabunites[self.ld]}{'s' if self.pd>1 else ''}" if self.pd!=0 else ''
        return f"{self.pe} unité{'s' if self.pe>1 else ''} {partiedec}"
    def fractiondec(self):
        return r"$\frac{" +str(self.pe*self.ud + self.pd) +r"}{" +str(self.ud)+"}$"
    def somme(self):
        res = str(self.pe)
        ppd=self.pd
        if ppd==0:
            return "$"+res+"$"
        res=[res]
        chiffres="0"*(self.ld - len(str(ppd))) +str(ppd)
        for i in range(len(chiffres)):
            if chiffres[i]!="0":
                res+=[r"\frac{" + chiffres[i] +"}{" + str(10**(i+1)) +"}"]
        return "$" + "+".join(res) + "$"
    def dec(self):
        return "$" +str(self.pe) + (("{,}" + "0"*(self.ld - len(str(self.pd))) +str(self.pd)) if self.pd!=0 else "") + "$"


def tirer_nombre(cmin=1, cmax=3): #Tire au sort un nombre pour le nombre de décimales
    nombredec=randint(cmin,cmax)
    tirer=0
    while tirer%10==0:
        tirer = randint(1, 10**nombredec-1)
    haszero = (tirer < 10**(nombredec-1)) or ("0" in str(tirer))  
    return tirer, nombredec, haszero


def generer_elements(nb_gen = 4):
    # Un seul élément à retourner : decimaux fraction 
    # bon ben je tire au sort des nombres. Genre 4. Au moins 2 d'entre eux doivent contenir un zéro à une position non dernière.
    nombres=[]
    for i in range(2):
        hz=False
        while not hz:
            pe, _, _= tirer_nombre()
            pd, nbd, hz = tirer_nombre()
        numbergot = str(pe) + "." + "0"* (nbd-len(str(pd))) + str(pd)
        nombres+=[numbergot]
    for i in range(2):
        pe, _, _= tirer_nombre()
        pd, nbd, hz = tirer_nombre()
        numbergot = str(pe) + "." + "0"* (nbd-len(str(pd))) + str(pd)
        nombres+=[numbergot]
    
    shuffle(nombres)
    # nombres contient maintenant les 4 nombres à foutre dans le tableau.  Je dois choisir lequel est lequel.

    for k in nombres:
        n = wdec(k)
        print(k, n.lecture(), n.fractiondec(), n.somme(), n.dec())

    ordre = [0,1,2,3]
    shuffle(ordre)

    textes = []
    for i in range(len(nombres)):
        n =wdec(nombres[i])
        functions = [n.lecture(), n.fractiondec(), n.somme(), n.dec()]

        toadd= [ functions[k] if k==ordre[i] else fr"\Texteouvide{{{functions[k]}}}" for k in range(4)]
        textes += [" & ".join(toadd)] 
        
    
    tablocomplet = " \\\\ \\hline \n".join(textes)

    print(tablocomplet)
    return {"tableau_fractions" : tablocomplet}


from template_management import load_template

def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)