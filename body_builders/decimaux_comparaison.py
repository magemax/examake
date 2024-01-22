
from random import randint, sample, choice, shuffle


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


modeles = [("0.123", "0.45"), ("30.456", "31.23"), ("3.456", "3.12"), ("0.14", "0.23")]

def tirer_nombre(): #Fait des comparaison
    tocompare=[]
    #("0.123", "0.45")
    pe=randint(1,99)
    pd1,pd2=0,0
    while pd1//10==pd2//10:
        pd1,pd2=sorted([randint(100,999), randint(100,999)])
    tc = (str(pe)+"{,}"+str(pd1) , str(pe)+"{,}"+str(pd2//10), 0)
    tocompare+=[tc]
    #("30.456", "31.23")
    a=randint(1,8)
    ap=a+1
    rd2=randint(1,99)*10
    pe1=rd2+a
    pe2 = rd2+ap
    pd1,pd2=0,0
    while pd1==pd2:
        pd1,pd2=sorted([randint(100,999), randint(100,999)])
    tc = (str(pe1)+"{,}"+str(pd2) , str(pe2)+"{,}"+str(pd1//10), 0)
    tocompare+=[tc]
    #("3.456", "3.12")
    pe=randint(1,99)
    pd1,pd2=0,0
    while pd1//10==pd2//10:
        pd1,pd2=sorted([randint(100,999), randint(100,999)])
    tc = (str(pe)+"{,}"+str(pd1//10) , str(pe)+"{,}"+str(pd2), 0)
    tocompare+=[tc]
    #("0.14", "0.23")
    pe=randint(1,9)
    pd1,pd2=0,0
    while pd1>=pd2 or pd2%10 >=pd1%10:
        pd1,pd2 = sorted([randint(11, 99), randint(11, 99)])
    tc=(str(pe)+"{,}"+str(pd1//10) , str(pe)+"{,}"+str(pd2), 0)
    tocompare+=[tc]

    # Un zéro au milieu
    a=0
    while a%10==0:
        a=randint(1111, 9999)    
    where=randint(1,3)
    t1=str(a)
    t1=t1[0]+"{,}"+t1[1:]
    t2=t1[:3+where]+"0"+t1[3+where:]
    tc=(t2, t1, 0)
    tocompare+=[tc]
    #("3.456", "3.123")
    pe=randint(1,99)
    pd1,pd2=0,0
    while pd1==pd2:
        pd1,pd2=sorted([randint(100,999), randint(100,999)])
    tc = (str(pe)+"{,}"+str(pd1) , str(pe)+"{,}"+str(pd2), 0)
    tocompare+=[tc]


    #("0.123", "0.45")
    pe=randint(1,99)
    pd1,pd2=0,0
    while pd1//10==pd2//10:
        pd1,pd2=sorted([randint(100,999), randint(100,999)])
    tc = (str(pe)+"{,}"+str(pd1) , str(pe)+"{,}"+str(pd2//10), 0)
    tocompare+=[tc]
    #("30.456", "31.23")
    a=randint(1,8)
    ap=a+1
    rd2=randint(1,99)*10
    pe1=rd2+a
    pe2 = rd2+ap
    pd1,pd2=0,0
    while pd1==pd2:
        pd1,pd2=sorted([randint(100,999), randint(100,999)])
    tc = (str(pe1)+"{,}"+str(pd2) , str(pe2)+"{,}"+str(pd1//10), 0)
    tocompare+=[tc]
    #("3.456", "3.12")
    pe=randint(1,99)
    pd1,pd2=0,0
    while pd1//10==pd2//10:
        pd1,pd2=sorted([randint(100,999), randint(100,999)])
    tc = (str(pe)+"{,}"+str(pd1//10) , str(pe)+"{,}"+str(pd2), 0)
    tocompare+=[tc]
    #("0.14", "0.23")
    pe=randint(1,9)
    pd1,pd2=0,0
    while pd1>=pd2 or pd2%10 >=pd1%10:
        pd1,pd2 = sorted([randint(11, 99), randint(11, 99)])
    tc=(str(pe)+"{,}"+str(pd1//10) , str(pe)+"{,}"+str(pd2), 0)
    tocompare+=[tc]

    # Un zéro au milieu
    a=0
    while a%10==0:
        a=randint(1111, 9999)    
    where=randint(1,3)
    t1=str(a)
    t1=t1[0]+"{,}"+t1[1:]
    t2=t1[:3+where]+"0"+t1[3+where:]
    tc=(t2, t1, 0)
    tocompare+=[tc]
    for t in tocompare:
        print(t)
    #("3.456", "3.123")
    pe=randint(1,99)
    pd1,pd2=0,0
    while pd1==pd2:
        pd1,pd2=sorted([randint(100,999), randint(100,999)])
    tc = (str(pe)+"{,}"+str(pd1) , str(pe)+"{,}"+str(pd2), 0)
    tocompare+=[tc]

    rtc = tocompare[:6] + sample(tocompare[6:], 2)
    rrtc=[]
    for k in rtc:
        if randint(0,1):
            rrtc+=[k]
        else:
            rrtc+=[(k[1],k[0],1)]

    res=[f"\\item ${k[0]} \\Sicorrection{{{'<' if k[2]==0 else '>'}}}{{\\cdots}} {k[1]}$" for k in rrtc]
    tableau_compa="\n".join(res)
    return {"liste_comparaisons" : tableau_compa}



def generer_elements():
    return tirer_nombre()


from template_management import load_template

def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)