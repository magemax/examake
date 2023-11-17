from template_management import load_template

import body_builders.thales_normal
import body_builders.thales_indirect
from random import choice


class ExoBrevet:
    def __init__(self, annee, question, corrige):
        self.annee= annee
        self.question = question
        self.corrige = corrige


LesExos=[]


annee = "DNB - Juin 2013 - Amérique du Nord"
question =r"""
Tom doit calculer $3,5^2$.
 
\og Pas la peine de prendre la calculatrice \fg, lui dit Julie, tu n'as qu'à effectuer le produit de $3$ par $4$ et rajouter $0,25$. 

\medskip

\begin{enumerate}
\item Effectuer le calcul proposé par Julie et vérifier que le résultat obtenu est bien le carré de $3,5$. 
\item Proposer une façon simple de calculer $7,5^2$ et donner le résultat. 
\item Julie propose la conjecture suivante : 	$(n + 0,5)^2 = n(n + 1) + 0,25$ 

$n$ est un nombre entier positif. 

Prouver que la conjecture de Julie est vraie (quel que soit le nombre $n$) 
\end{enumerate} 
"""

corrige = r"""
\begin{enumerate}
\item %Effectuer le calcul proposé par Julie et vérifier que le résultat obtenu est bien le carré de $3,5$.
$3 \times 4  + 0,25 = 12 + 0,25 = 12,25$.

Or $3,5^2 = \left(\dfrac{7}{2} \right)^2 = \dfrac{7^2}{2^2} = \dfrac{49}{4} = \dfrac{24,5}{2} = 12,25$. Le calcul est exact. 
\item %Proposer une façon simple de calculer $7,5^2$ et donner le résultat.
Multiplier 7 par 8 et ajouter 0,25 au produit.

$7 \times 8 + 0,25 = 56,25$.

$7,5^2 = \left(\dfrac{15}{2} \right)^2 = \dfrac{15^2}{2^2} = \dfrac{225}{4} = \dfrac{112,5}{2} = 56,25$. Exact ! 
\item %Julie propose la conjecture suivante : 	$(n + 0,5)^2 = n(n + 1) + 0,25$ 

%$n$ est un nombre entier positif. 

%Prouver que la conjecture de Julie est vraie (quel que soit le nombre $n$)
Quel que soit le naturel $n$ : $(n + 0,5)^2 = n^2 + 0,5^2 + 2 \times n \times 0,5 = n^2 + n + 0,25 = n(n + 1) + 0,25$.

La  conjecture de Julie est vraie.
\end{enumerate} 
"""

LesExos+= [ExoBrevet(annee, question, corrige)]

annee = "DNB - Juin 2015 - Métropole"

question = r"""
Voici un programme de calcul sur lequel travaillent quatre élèves.

\begin{center}
\begin{tabular}{|p{0.4\linewidth}|}\hline
$\bullet~~$ Prendre un nombre\\
$\bullet~~$ Lui ajouter 8\\
$\bullet~~$ Multiplier le résultat par 3\\
$\bullet~~$ Enlever 24\\
$\bullet~~$ Enlever le nombre de départ\\\hline
\end{tabular}
\end{center}


Voici ce qu'ils affirment :

Sophie : \og Quand je prends 4 comme nombre de
départ, j'obtiens, 8 \fg

Martin : \og En appliquant le programme à 0, je trouve 0. \fg

Gabriel : \og  Moi,j'ai pris $-3$ au départ et j'ai obtenu $-9$. \fg

Faïza : \og Pour n'importe quel nombre choisi, le résultat final est égal au double du nombre de départ. \fg

Pour chacun de ces quatre élèves expliquer en justifiant vore réponse s'il a raison ou tort.
"""

corrige= r"""
Si on appelle $x$ le nombre de départ, le programme de calcul devient alors :\\
$3(x+8)-24-x=3x+24-24-x=2x$.

Sophie, Martin et Faïza ont donc raison tandis que Gabriel se trompe.
"""

LesExos+= [ExoBrevet(annee, question, corrige)]

annee = "DNB - Avril 2014 - Pondichéry"


question = r"""\og Je prends un nombre entier. Je lui ajoute 3 et je multiplie le résultat par 7. J'ajoute le triple du nombre de départ au résultat et j'enlève 21. J'obtiens toujours un multiple de 10, c'est à dire un nombre de la forme $10k$, où $k$ est un nombre entier.\fg

\medskip

Est-ce vrai ? Justifier.
 
\textbf{Si travail n'est pas terminé, laisser tout de même une trace de la recherche. Elle sera prise en compte dans l'évaluation.}
 
"""
corrige = r"""
Soit $x$ le nombre de départ.

Ajoutons 3 : $x + 3$. Multiplions le résultat par 7 : $7\times (x + 3) = 7\times x+7\times 3 = 7x + 21$.

Ajoutons le triple du nombre de départ au résultat : $7x + 21 + 3\times x = 10x + 21$.

Enlevons 21 au résultat : $10x + 21 - 21 = 10x$.

L'affirmation est donc  vraie.

"""


LesExos+= [ExoBrevet(annee, question, corrige)]


annee = "DNB Juin 2015 Amérique du Nord"

question = r"""Trouver le nombre auquel je pense, en expliquant votre raisonnement

\setlength\parindent{1.5cm}
\begin{itemize}
\item[$\bullet~~$] Je pense à un nombre.
\item[$\bullet~~$] Je lui soustrais $10$.
\item[$\bullet~~$] J'élève le tout au carré.
\item[$\bullet~~$] Je soustrais au résultat le carré du nombre auquel j'ai pensé.
\item[$\bullet~~$] J'obtiens alors : $- 340$.
\end{itemize}
\setlength\parindent{0cm}
"""

corrige = r"""
Notons $x$ le nombre auquel l'on pense.

$\bullet~~$	$x$

$\bullet~~$	$x - 10$

$\bullet~~$	$(x - 10)^2 = (x - 10)(x - 10) = x^2 - 10x - 10x + 100 = x^2 - 20x + 100$

$\bullet~~$	$x^2 - 20x + 100 - x^2 = - 20x + 100$

Le résultat obtenu est : $- 20x + 100$.

On résout l'équation :	$- 20x + 100	=	- 340$

				$- 20x	=	-440$
				
				$20x	=	440$
				
				$x	=	22$.
				
Le nombre auquel on pense au départ est donc $22$.
"""

LesExos+= [ExoBrevet(annee, question, corrige)]


def generer_elements():
    whom= choice(LesExos)
    d={}
    d["annee"]=whom.annee
    d["question"]=whom.question
    d["corrige"]=whom.corrige
    return d


def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = generer_elements()

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)