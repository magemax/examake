# Exercice : Donner une liste de 15 entiers, déterminer les nombres premiers
# 0, 1, 2, 3, 4, 5  ===>  3 parmi 6
# Entre 6 et 50 ===> 7
# 50 ou + ===>   5
# Exercice : Donner une liste de 15 entiers, déterminer les nombres premiers
# 0, 1, 2, 3, 4, 5  ===>  3 parmi 6
# Entre 6 et 50 ===> 7
# 50 ou + ===>   5
from template_management import load_template
from random import randint



def gen_primes(n):
    """ Generate prime numbers until n
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    Dr={}
    
    # The running integer that's checked for primeness
    q = 2
    while q<=n:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            Dr[q]=None
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1
    return Dr.keys()


def decompprime(n,primesorted):
    r={}
    j=0
    i=0
    while n>1 and i*i<n:
        i=primesorted[j]
        ri=0
        while n%i==0:
            n//=i
            ri+=1
        if ri>0:
            r[i]=ri
        j+=1
    if n>1:
        r[n]=1
    return r

primes=sorted(gen_primes(100))

def dcptotext(dcp):
    res=[]
    for k,v in dcp.items():
        if (v>1):
            res+=[f"{k}^{v}"]
        else:
            res+=[f"{k}"]
    return r"\times".join(res)

def generer_elements():
    
    nombre=randint(2,300)
    dcp= decompprime(nombre, primes)
    while len(dcp)<3 or len(dcp)>5:
        nombre=randint(2,300)
        dcp= decompprime(nombre, primes)



    d={}
    d["nombre"] = nombre
    d["decomposition"] = dcptotext(dcp)
    return d



def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)
