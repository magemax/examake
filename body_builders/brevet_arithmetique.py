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


annee = "Décembre 2016 Amérique du sud"
question =r"""
Carole souhaite réaliser une mosaïque sur un mur de sa maison. La surface à paver est un
rectangle de dimensions $108$~cm et $225$~cm et doit être entièrement recouverte par des carreaux
de faïence carrés de même dimension sans découpe.

\medskip

\begin{enumerate}
\item Carole peut-elle utiliser des carreaux de 3~cm de côté ? De 6~cm de côté ?
\item Quelle est la dimension maximale des carreaux que Carole peut poser ?

Combien de carreaux utilisera-t-elle ?
\end{enumerate}
"""

corrige = r"""
On suppose ici que la surface mesure $108$~cm de large et $225$~cm de long (les résultats seraient les mêmes si les dimensions étaient inversées par une rotation).

\begin{enumerate}
\item Il faut que la longueur et la largeur du rectangle soient multiples de 3 ce qui est le cas car :

$108 = 3 \times 36$ et $225 = 3 \times 75$.

36 carreaux en largeur et 75 en longueur : Carole pourra paver la surface avec $36 \times 75 = 2700$ carreaux.

Il est facile de calculer l'aire de la surface totale que devra paver Carole. Il ne s'agit rien d'autre que de l'aire du rectangle.

$A_R =  225 \times 108 = 24300~\left(\text{cm}^2\right)$.

%Si elle utilise des carreaux de 3~cm de côté, cela signifie que la surface de chaque carreau, soit l'aire d'un carreau, est égale à : $3 \times 3 = 9~\left(\text{cm}^2\right)$.
%En divisant l'aire du rectangle par l'aire d'un carreau, on obtiendra le nombre de carreaux nécessaires pour paver la totalité de la mosaïque. Si ce nombre est un entier, alors Carole pourra utiliser des carreaux de 3~cm de côté. Or
%
%$\dfrac{24300}{9} = 2700$
%
%Avec des carreaux de 3 cm de côté, Carole aura donc besoin de 2700 carreaux pour paver sa surface.

On ne peut pas utiliser des carreaux de 6~cm de côté. En effet en longueur il faudrait que 6 divise 225, ce qui est faux.
\item Pour déterminer la dimension maximale des carreaux qu'elle peut utiliser, il faut commencer par chercher le plus grand diviseur commun de 225 et de 108. 
En effet, étant donné que les carreaux sont des carrés, ils doivent avoir la même longueur et la même largeur.

Les diviseurs de 225 sont: 1-3-5-9-15-25-45-75-225.

Les diviseurs de 108 sont: 1-2-3-4-6-9-12-18-27-36-54-108.

On remarque que 9 est le plus grand diviseur commun des deux nombres. Il faut donc que Carole utilise des carreaux de 9 cm de côté, cette dimension étant la plus grande qu'elle puisse utiliser.

Etant donné que la surface à paver est de 24300~cm$^2$, et que chaque carré a une aire de 

$9 \times 9 = 81~\left(\text{cm}^2\right)$,
il faudra utiliser au total : $\dfrac{24300}{81} = 300$~carreaux de 9~cm de côté.
\end{enumerate}

"""

LesExos+= [ExoBrevet(annee, question, corrige)]


annee = "DNB Décembre 2017 Nouvelle Calédonie"
question =r"""

\medskip

--- AUREL : Belle pêche ! Combien de poissons et de coquillages vas-tu pouvoir vendre au marché ?

--- ANTOINE : En tout, je vais pouvoir vendre au marché 30 poissons et 500 coquillages.

\medskip

Antoine est un pêcheur professionnel. Il veut vendre des paniers contenant des coquillages et des
poissons. Il souhaite concevoir le plus grand nombre possible de paniers identiques. Enfin, il voudrait qu'il ne lui reste aucun coquillage et aucun poisson dans son congélateur.

\medskip

\begin{enumerate}
\item Combien de paniers au maximum Antoine pourra t-il concevoir ? Justifier.
\item Quelle sera la composition de chaque panier ? Justifier.
\end{enumerate}

"""

corrige = r"""
"""

LesExos+= [ExoBrevet(annee, question, corrige)]

annee = "2014 - Pondichéry"
question =r"""
\medskip

Flavien veut répartir la totalité de 760~dragées au chocolat et 1045~dragées aux amandes dans des sachets dans des sachets ayant la même répartition de dragées au chocolat et aux amandes.

\medskip
 
\begin{enumerate}
\item Peut-il faire 76 sachets ? Justifier la réponse. 
\item 
	\begin{enumerate}
		\item Quel nombre maximal de sachets peut-il réaliser ? 
		\item Combien de dragées de chaque sorte y aura-t-il dans chaque sachet?
	\end{enumerate}
\end{enumerate}

"""

corrige = r"""
\begin{enumerate}
\item %Peut-il faire 76 sachets ? Justifier la réponse.
On a $760 = 76 \times 10$ mais  $1045$ impair ne peut être multiple de 76 qui est pair. On ne peut donc répartir ces dragées dans 76 sachets.
\item 
	\begin{enumerate}
		\item %Quel nombre maximal de sachets peut-il réaliser ?
		On cherche avec l'algorithme d'Euclide le PGCD à 760 et 1045 :
		
$1045 = 760 \times 1 + 285$ ;

$760 = 285 \times 2 + 190$ ;

$285 = 190 \times 1 + 95$ ;

$190 = 95 \times 2 + 0$.

On a donc $PGCD(760~;~1045) = 95$.

On peut faire au maximum 95 sachets. 
		\item %Combien de dragées de chaque sorte y aura-t-il dans chaque sachet ?
On  a $760 = 95 \times 8$ et $1045 = 95 \times 11$.

Il y a dans chacun des 95 sachets, 8 dragées au chocolat et 11 dragées aux amandes.
	\end{enumerate}
\end{enumerate}
"""

LesExos+= [ExoBrevet(annee, question, corrige)]

annee = "2013 - Polynésie"
question =r"""

\begin{enumerate}
\item Calcule PGCD(405~;~315). Précise la méthode utilisée et indique les calculs. 
\item Dans les bassins d'eau de mer filtrée d'une ferme aquacole de bénitiers destinés à l'aquariophilie, on compte $9$ bacs contenant chacun $35$ bénitiers de $12,5$~cm et $15$~bacs contenant chacun $27$~bénitiers de $17,5$~cm.
 
L'exploitant souhaite répartir la totalité des bénitiers en des lots de même composition :
 
Par lot, même nombre de bénitiers de $12,5$~cm et même nombre de bénitiers de $17,5$~cm. 
	\begin{enumerate}
		\item Quel est le plus grand nombre de lots qu'il pourra réaliser ? Justifie ta réponse. 
		\item Quelle sera la composition de chaque lot ? 
	\end{enumerate}
\end{enumerate}
"""

corrige = r"""

\begin{enumerate}
\item %Calcule PGCD(405~;~315). Précise la méthode utilisée et indique les calculs.
On a successivement avec l'algorithme d'Euclide :

$405 = 315 \times 1 + 90$ ;

$315 = 90 \times 3 + 45$ ; 

$90 = 45 \times 2$.

On a donc  PGCD(405~;~315) = 45.
\item %Dans les bassins d'eau de mer filtrée d'une ferme aquacole de bénitiers destinés à l'aquariophilie, on compte $9$ bacs contenant chacun $35$ bénitiers de $12,5$~cm et $15$~bacs contenant chacun $27$~bénitiers de $17,5$~cm.
 
%L'exploitant souhaite répartir la totalité des bénitiers en des lots de même composition :
 
%Par lot, même nombre de bénitiers de $12,5$~cm et même nombre de bénitiers de $17,5$~cm. 
On a donc$9\times 35 = 315$ petits bénitiers et $15 \times 27 = 405$ grands bénitiers.
	\begin{enumerate}
		\item %Quel est le plus grand nombre de lots qu'il pourra réaliser ? Justifie ta réponse.
D'après la question précédente on pourra faire 45 lots . 
		\item %Quelle sera la composition de chaque lot ?
Chaque lot contient  7 petits et 9 grands 
	\end{enumerate}
\end{enumerate}
"""

LesExos+= [ExoBrevet(annee, question, corrige)]

annee = "2015 - Pondichéry"
question =r"""
Un chocolatier vient de fabriquer 2622~oeufs de Pâques et 2530~poissons en chocolat.

Il souhaite vendre des assortiments d'oeufs et de poissons de façon que:

\setlength\parindent{6mm}
\begin{itemize}
\item[$\bullet~~$] tous les paquets aient la même composition ;
\item[$\bullet~~$] après mise en paquet, il reste ni oeufs, ni poissons.
\end{itemize}
\setlength\parindent{0mm}

\medskip

\begin{enumerate}
\item Le chocolatier peut-il faire 19 paquets ? Justifier.
\item Quel est le plus grand nombre de paquets qu'il peut réaliser ? Dans ce cas, quelle
sera la composition de chaque paquet ?
\end{enumerate}
"""

corrige = r"""
\begin{enumerate}
\item %Le chocolatier peut-il faire 19 paquets ? Justifier.
On a $\dfrac{2622}{19} = 138$, mais $\dfrac{2530}{19} \approx  133,2$.

Ce qui veut dire que l'on ne pas répartir les 2530 poissons dans 19 paquets (il en reste 3)
\item %Quel est le plus grand nombre de paquets qu'il peut réaliser ? Dans ce cas, quelle sera la composition de chaque paquet ?
Le plus grand nombre de paquets qu'il peut réaliser est un diviseur commun à 2622 et à 2530. Puisque c'est le plus grand c'est donc leur PGCD que l'on calcule grâce à l'algorithme d'Euclide :

$2622  2530 \times 1 + 92$ ;

$2530 =  92 \times 27  + 46$ ;

$92 = 46 \times 2 + 0$.

Le PGCD est le dernier reste non nul, donc 46.

Effectivement : $\dfrac{2622}{46} = 57$ et   $\dfrac{2530}{46} = 55$

Dans chacun des 46 paquets il y aura 57 œufs et 55 poissons.
\end{enumerate}
"""

LesExos+= [ExoBrevet(annee, question, corrige)]

annee = "2021 - Métropole"
question =r"""
Un professeur organise une sortie pédagogique au Futuroscope pour ses élèves de troisième. Il veut répartir les $126$ garçons et les $90$ filles par groupes. Il souhaite que chaque groupe comporte le même nombre de filles et le même nombre de garçons.
	\begin{enumerate}
		\item Décomposer en produit de facteurs premiers les nombres $126$ et $90$
		\item Trouver tous les entiers qui divisent à la fois les nombres $126$ et $90$.
		\item En déduire le plus grand nombre de groupes que le professeur pourra
constituer. 

Combien de filles et de garçons y aura-t-il alors dans chaque groupe?
	\end{enumerate}
"""

corrige = r"""
\begin{enumerate}
        \item $126=2\times 3^{2}\times7$ et $90=2\times 3^{2}\times5$.
        \item Les diviseurs de $126$ sont : 1; 2; 3; 6; 7; 9; 14; 18; 21; 42; 63; 126.\\ Les diviseurs de $90$ sont 1; 2; 3; 5; 6; 9; 10; 15; 18; 30; 45; 90.
        \item Pour faire un groupe qui respecte les conditions de l'énoncé, le nombre de groupes doit être un diviseur commun à $126$ et à $90$.\\
        On déduit de la question précédente que les diviseurs communs de $90$ et $126$ sont : 1; 2; 3; 6; 9 et 18.\\
        Le plus grand nombre de groupes est donc le plus grand diviseur commun à 126 et 90 à savoir 18  .\\
        On peut noter ainsi : $PGCD(126;90)=18$\\
        \textbf{Le professeur pourra donc faire 18 groupes de 7 garçons et 5 filles chacun.}
    \end{enumerate}
"""

LesExos+= [ExoBrevet(annee, question, corrige)]

annee = "Décembre 2020 - Nouvelle Calédonie"
question =r"""
\begin{enumerate}
\item Justifier que le nombre 102 est divisible par 3.
\item On donne la décomposition en produits de facteurs premiers de 85 : $85 = 5 \times 17$.

Décomposer 102 en produits de facteurs premiers.
\item Donner 3 diviseurs non premiers du nombre 102.
\end{enumerate}

Un libraire dispose d'une feuille cartonnée de 85 cm sur 102 cm.

Il souhaite découper dans celle-ci, en utilisant toute la feuille, des étiquettes carrées. 

Les côtés de ces étiquettes ont tous la même mesure.
\begin{enumerate}
\item Les étiquettes peuvent-elles avoir $34$ cm de côté ? Justifier. 
\item Le libraire découpe des étiquettes de $17$ cm de côté.

Combien d'étiquettes pourra-t-il découper dans ce caenums ?
\end{enumerate}
"""

corrige = r"""

\begin{enumerate}
\item %Justifier que le nombre 102 est divisible par 3.
$\bullet~~$Comme $1 + 0 + 2 = 3$, 102 est un multiple de 3 (critère de divisibilité par 3 ;

$\bullet~~$$102 = 90 + 12 = 3\times 30 + 3 \times 4 = 3\times (30 + 4) = 3\times 34$.

102 est un multiple de 3  : il est divisible par 3.
\item On donne la décomposition en produits de facteurs premiers de 85 : $85 = 5 \times 17$.

%Décomposer 102 en produits de facteurs premiers.
On a vu que $102 = 3 \times 34 = 3 \times 2 \times 17 = 2 \times 3 \times 17$.
\item Donner 3 diviseurs non premiers du nombre 102.

$2 \times 3 = 6 \:;\:  2 \times 17 = 34 \:;\: 3 \times 17 = 51$ sont trois diviseurs de 102 non premiers. 
%\end{enumerate}

%Un libraire dispose d'une feuille cartonnée de 85 cm sur 102 cm.
%
%Il souhaite découper dans celle-ci, en utilisant toute la feuille, des étiquettes carrées. 
%
%Les côtés de ces étiquettes ont tous la même mesure.
%\begin{enumerate}
\item %Les étiquettes peuvent-elles avoir $34$ cm de côté ? Justifier. 
Si toute la feuille est utilisée c'est que la longueur et la largeur sont des multiples des côtés du carré. Ces côtés ont donc une  longueur $c$ qui divise à la fois 102 et 85.

Or 34 ne divise pas 85 (car 2 divise 34 mais ne divise pas 85). les étiquettes ne peuvent pas faire 34cm de côté.
\item %Le libraire découpe des étiquettes de $17$ cm de côté.

%Combien d'étiquettes pourra-t-il découper dans ce cas ?
Par contre 17 divise 85 ($85 = 5 \times 17$) et 17 divise 102 ($102 = 17 \times 6$).

Les étiquettes rentrent 5 fois en largeur et 6 fois en longueur : il y en aura donc $5 \times 6 = 30$ par feuille.

\emph{Remarque } : on peut aussi utiliser les aires.

Une étiquette a une aire de $17 \times 17 = 289$ et la feuille une aire de $85 \times 102 = 8670$.

On pourra donc faire $\dfrac{8670}{289} = 30$ étiquettes dans une feuille.
\end{enumerate}
"""

LesExos+= [ExoBrevet(annee, question, corrige)]


annee = "DNB Juin 2015 Asie"
question =r"""
À la fin d'une fête de village, tous les enfants présents se partagent équitablement les 397
ballons de baudruche qui ont servi à la décoration. Il reste alors 37 ballons. 

\smallskip

L'année suivante, les mêmes enfants se partagent les 598 ballons utilisés cette année-là.
Il en reste alors 13.

\smallskip

Combien d'enfants, au maximum, étaient présents ?

\emph{Toute trace de recherche, même incomplète, sera prise en compte dans le notation.}

\vspace{0,5cm}
"""

corrige = r"""
%À la fin d'une fête de village, tous les enfants présents se partagent équitablement les 397
%ballons de baudruche qui ont servi à la décoration. Il reste alors 37 ballons. 
%
%\smallskip
%
%L'année suivante, les mêmes enfants se partagent les 598 ballons utilisés cette année-là.
%Il en reste alors 13.
%
%\smallskip
%
%Combien d'enfants, au maximum, étaient présents ?

%\emph{Toute trace de recherche, même incomplète, sera prise en compte dans le notation.}
S’il reste 37 ballons la première année, les enfants se sont partagés équitablement 360
ballons car $397 - 37 = 360$.

S’il reste 13 ballons l'année suivante, les enfants se sont partagés équitablement 585
ballons car $598 - 13 = 585$.

Pour connaître le nombre maximum d’enfants présents à la fête, je recherche le PGCD,
plus grand diviseur commun à $360$ et $585$. J’utilise l’algorithme d’Euclide.

$585 = 360 \times 1 + 225$

$360 = 225 \times 1 + 135$

$225 =135 \times 1 + 90$

$135 = 90 \times 1 + 45$

$90 = 45 \times 2 + 0$

Le dernier reste non nul est 45, donc PGCD$(585~;~360) = 45$.

Le nombre maximum d’enfants présents était de $45$.
\vspace{0,5cm}
"""

#LesExos+= [ExoBrevet(annee, question, corrige)]

annee = "DNB 2018 Métropole"
question =r"""
\begin{enumerate}
\item Le nombre $588$ peut se décomposer sous la forme $588 = 2^2 \times  3 \times 7^2$.

Quels sont ses diviseurs premiers, c'est-à-dire les nombres qui sont à la fois des nombres premiers et des diviseurs de $588$ ?
\item 
	\begin{enumerate}
		\item Déterminer la décomposition en facteurs premiers de 27000000.
		\item Quels sont ses diviseurs premiers ?
	\end{enumerate}
\item Déterminer le plus petit nombre entier positif impair qui admet trois diviseurs premiers différents. Expliquer votre raisonnement.
\end{enumerate}
"""

corrige = r"""

\begin{enumerate}
\item Le nombre $588$ peut se décomposer sous la forme $588 = 2^2 \times  3 \times 7^2$.

%Quels sont ses diviseurs premiers, c'est-à-dire les nombres qui sont à la fois des nombres premiers et des diviseurs de $588$ ?
Les diviseurs premiers de 588 sont 2~;~3 et 7.
\item 
	\begin{enumerate}
		\item %Déterminer la décomposition en facteurs premiers de 27000000.
$27000000 = 27 \times 1000000 = 3^3 \times 10^6 = 3^3 \times (2 \times 5)^{6} = 3^3 \times 2^6 \times 5^6 = 2^6 \times 3^3 \times 5^6$.
		\item %Quels sont ses diviseurs premiers ?
		Les diviseurs premiers de 27000000 sont 2~;~3 et 5
	\end{enumerate}
\item %Déterminer le plus petit nombre entier positif impair qui admet trois diviseurs premiers différents. Expliquer votre raisonnement.
Les premiers nombres impairs premiers sont 3~;~5 et 7, donc le plus petit entier impair admettant trois diviseurs premiers différents est $3 \times 5 \times 7 = 105$.
\end{enumerate}
"""

#LesExos+= [ExoBrevet(annee, question, corrige)]

annee = "DNB Décembre 2018 Nouvelle Calédonie"
question =r"""
\begin{enumerate}
\item Décomposer les nombres $162$ et $108$ en produits de facteurs premiers.
\item Déterminer deux diviseurs communs aux nombres $162$ et $108$ plus grands que $10$.
\item Un snack vend des barquettes composées de nems et de samossas.

Le cuisinier a préparé $162$ nems et $108$ samossas.

Dans chaque barquette :

\setlength\parindent{9mm}
\begin{itemize}
\item le nombre de nems doit être le même.
\item le nombre de samossas doit être le même,
\end{itemize}
\setlength\parindent{0mm}

Tous les nems et tous les samossas doivent être utilisés.
	\begin{enumerate}
		\item Le cuisiner peut-il réaliser $36$ barquettes ?
		\item Quel nombre maximal de barquettes pourra-t-il réaliser ?
		\item Dans ce cas, combien y aura-t-il de nems et de samossas dans chaque barquette ?
	\end{enumerate}
\end{enumerate}
"""

corrige = r"""
\begin{enumerate}
\item %Décomposer les nombres $162$ et $108$ en produits de facteurs premiers.
$162 = 2 \times 81 = 2 \times 9 \times 9 = 2 \times 3^2 \times 3^2 = 2 \times 3^4$.

$108 = 2 \times 54 = 2 \times 2 \times 27 = 2^2 \times 3^3$.
\item %Déterminer deux diviseurs communs aux nombres $162$ et $108$ plus grands que $10$.
Les diviseurs communs à 162 et 108 sont : 1 ; 2 ; 3 ;  6 ; 9 ; 18 ; 27 et 54.
\item %Un snack vend des barquettes composées de nems et de samossas.

%Le cuisinier a préparé $162$ nems et $108$ samossas.

%Dans chaque barquette :
%
%\setlength\parindent{9mm}
%\begin{itemize}
%\item le nombre de nems doit être le même.
%\item le nombre de samossas doit être le même,
%\end{itemize}
%\setlength\parindent{0mm}
%
%Tous les nems et tous les samossas doivent être utilisés.
	\begin{enumerate}
		\item %Le cuisiner peut-il réaliser $36$ barquettes ?
Le cuisiner ne peut pas  réaliser $36$ barquettes car 36 ne divise pas 162.
		\item %Quel nombre maximal de barquettes pourra-t-il réaliser ?
		Le plus grand commun diviseur à 162 et 108 est 54 ; le cuisinier peut donc préparer 54 barquettes. 
		\item %Dans ce cas, combien y aura-t-il de nems et de samossas dans chaque barquette ?
Chaque barquette contiendra alors  3 nems et 2 samoussas.
	\end{enumerate}
\end{enumerate}
"""

#LesExos+= [ExoBrevet(annee, question, corrige)]

annee = "DNB Juillet 2019 Métropole"
question =r"""
Le capitaine d'un navire possède un trésor constitué de $69$ diamants, 1150 perles et 4140 pièces d'or.

\medskip

\begin{enumerate}
\item Décomposer 69 ; 1150 et 4140 en produits de facteurs premiers.
\item Le capitaine partage équitablement le trésor entre les marins.

Combien y-a-t-il de marins au maximum sachant que toutes les pièces, perles et diamants ont été distribués ?
\end{enumerate}

"""

corrige = r"""
\begin{enumerate}
\item On a $69 = 3 \times 23$,\: 

$1150 = 115 \times 10 = 5 \times 23  \times 2 \times 5 = 2 \times 5^2 \times 23$,
et 

$4140 = 414 \times 10 = 6 \times 69 \times 10 = 2 \times 3 \times 3 \times 23 \times 2 \times 5 = 2^2 \times 3^2 \times 5 \times 23$.

La liste des nombres premiers commence par :

2 – 3 – 5 – 7 – 11 – 13 – 17 – 19 – 23 – 29 …
\item  Le nombre de marins doit diviser 69, 1150 et 4140.

Seul le facteur 23 est commun aux trois décompositions.

Il y a donc 23 marins au maximum (le seul autre nombre de marins qui conviendrait est de 1).
\end{enumerate}
"""

LesExos+= [ExoBrevet(annee, question, corrige)]

annee = ""
question =r"""
"""

corrige = r"""
"""

#LesExos+= [ExoBrevet(annee, question, corrige)]


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