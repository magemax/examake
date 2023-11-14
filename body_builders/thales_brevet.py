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


annee = "DNB Novembre 2014 Amérique du sud"
question =r"""
Joachim doit traverser une rivière avec un groupe d'amis. 

Il souhaite installer une corde afin que les personnes peu rassurées puissent se tenir. 

Il veut connaître la largeur de la rivière à cet endroit (nommé D) pour déterminer si la corde dont il dispose est assez longue. 

Pour cela il a repéré un arbre (nommé A) sur l'autre rive. 

Il parcourt 20~mètres sur la rive rectiligne où il se situe et trouve un nouveau repère : un rocher (nommé R). 

Ensuite il poursuit sur 12 mètres et s'éloigne alors de la rivière, à angle droit, jusqu'à ce que le rocher soit aligné avec l'arbre depuis son point d'observation (nommé B). Il parcourt pour cela 15 mètres. 

Il est alors satisfait: sa corde d'une longueur de 30 mètres est assez longue pour qu'il puisse l'installer entre les points D et A. 

A l'aide de la figure, confirmer sa décision. 

\begin{center}
\psset{unit=1cm}
\begin{pspicture}(10,5)
%\psgrid
\psline(0,2)(10,2)\psline(0,4.5)(10,4.5)
\psline(0.5,2)(0.5,4.5)(6,0.25)(6,2)
\rput(8,3.25){Rivière} 
\uput[d](2,2){20~m} 
\uput[u](4.9,2){12~m}
\uput[r](6,1.25){15~m} 
\rput(2.5,0.5){\small La figure n'est pas à l'échelle}
\uput[ul](0.5,4.5){A} \uput[d](0.5,2){D}\uput[u](3.75,2){R}
\uput[u](6,2){V} \uput[r](6,0.5){B} 
\end{pspicture}
\end{center}
"""
corrige = r"""
Les droites (AD) et (BV) sont toutes les deux perpendiculaires à la droite (DV) : elles sont donc parallèles. Les points B, R, A d'une part, les points V, R, D d'autre part sont alignés dans cet ordre. On peut donc énoncer le théorème de Thalès :

\[\dfrac{\text{RV}}{\text{RD}} = \dfrac{\text{BV}}{\text{AD}} \:\text{ soit }\: \dfrac{12}{20} = \dfrac{15}{\text{AD}}\: \text{ d'où  AD }\: = \dfrac{15 \times 20}{12} = \dfrac{3 \times 5 \times 4 \times 5}{3 \times 4} = 25.\]

Comme $25 < 30$ il pourra effectivement installer sa corde entre les points A et D.
"""

LesExos+= [ExoBrevet(annee, question, corrige)]

annee = "DNB Juin 2015 Amérique du Nord"

question = r"""
Pour filmer les étapes d'une course cycliste, les réalisateurs de télévision utilisent des
caméras installées sur deux motos et d'autres dans deux hélicoptères. Un avion relais,
plus haut dans le ciel, recueille les images et joue le rôle d'une antenne relais.
On considère que les deux hélicoptères se situent à la même altitude et que le peloton  des coureurs roule sur une route horizontale. Le schéma ci-dessous illustre cette
situation:

\begin{center}
\psset{unit=0.8cm}
\begin{pspicture}(14,7)
%\psgrid
\psdots[dotstyle=+,dotangle=45](7,5.8)(1.8,0)(11.8,0)(3.8,2.2)(10,2.2)%AMNHJ
\uput[u](7,5.8){A (avion)} \uput[d](1.8,0){M (moto 2)} \uput[d](11.8,0){N (moto 1)} \uput[ul](3.8,2.2){H hélicoptère 2} \uput[ur](10,2.2){L hélicoptère 1} 
%\pspolygon(7,5.8)(1.8,0)(11.8,0)
\psline(0,0)(14,0)
\end{pspicture}
\end{center}

\medskip

L'avion relais (point A), le premier hélicoptère (point L) et la première moto (point N)
sont alignés. 

De la même manière, l'avion relais (point A), le deuxième hélicoptère
(point H) et la deuxième moto (point M) sont également alignés.

On sait que : AM = AN = 1 km ; HL = 270~m et AH = AL = 720~m.

\medskip

\begin{enumerate}
\item Relever la phrase de l'énoncé qui permet d'affirmer que les droites (LH) et (MN) sont
parallèles.
\item  Calculer la distance MN entre les deux motos.
\end{enumerate}
"""

corrige= r"""
\begin{enumerate}
\item %Relever la phrase de l'énoncé qui permet d'affirmer que les droites (LH) et (MN) sont parallèles.
On considère que les deux hélicoptères se situent à la même altitude et que le peloton des coureurs roule sur une route horizontale.
\item  %Calculer la distance MN entre les deux motos.
Dans le triangle AMN :	H $\in$ [AM], L $\in$ [AN] et (LH) // (MN), donc, d'après le théorème de Thalès :  

$\dfrac{\text{AH}}{\text{AM}}= \dfrac{\text{AL}}{\text{AN}} = \dfrac{\text{HL}}{\text{MN}}$, 

soit  $\dfrac{720}{\np{1000}}  =\dfrac{720}{\np{1000}} = \dfrac{270}{\text{MN}}$.

Donc MN $= \dfrac{270 \times \np{1000}}{720} = 375$~m.
\end{enumerate}"""

LesExos+= [ExoBrevet(annee, question, corrige)]

annee = "DNB Décembre 2013 Nouvelle Calédonie"


question = r"""
En se retournant lors d'une marche arrière, le conducteur d'une camionnette voit le sol à 6 mètres derrière son camion. 

Sur le schéma, la zone grisée correspond à ce que le conducteur ne voit pas lorsqu'il regarde en arrière. 

\begin{center}
\psset{unit=0.65cm}
\begin{pspicture}(17,4.75)
\pspolygon[fillstyle=solid,fillcolor=lightgray](6.35,0)(13.9,0)(6.35,2.7)%ECA
\pscurve(0,1)(0.1,1.3)(0.3,2)(0.4,2.5)(0.75,2.7)(1,3)(1.6,4)(1.8,4.2)(2,4.3)(2.4,4.4)(5,4.3)(6,4.2)(6.2,4)(6.4,3)(6.45,2.35)(6.6,2.3)(6.5,1.6)(6.35,1.6)(6.3,1.3)(6.1,1.3)(6,1)(6,0.8)(5.85,0.8)(5.8,1)(5.7,1.3)(5.2,1.6)(5,1.6)(4.5,1.4)(4.3,1)(4.2,0.7)(3,0.65)(2.3,0.7)(2.2,1)(2,1.4)(1.5,1.6)(1,1.4)(0.8,1)(0.7,0.7)(0.3,0.7)(0,1)
\pscurve(0.7,2.7)(1.2,2.7)(1.4,3)(1.8,4.2)
\pscurve(1.5,2.7)(2.8,2.7)(3,2.8)(3,3.2)(3.,4.1)(2,4.1)(1.8,3.5)(1.5,2.7)
\pscurve(3.2,2.7)(4.6,2.8)(4.6,3)(4.65,4.05)(3.3,4)(3.25,3.5)(3.2,2.7)
\pscurve(4.8,2.7)(6,2.65)(6.2,3)(6,4)(5.1,4.1)(4.9,3.7)(4.8,2.7)
\pscurve(0.4,2.5)(3,2.4)(6.3,2.4)
\pscurve(0.3,2.3)(2,2.2)(6.3,2.1)
\pscurve(1.5,0)(1,0.2)(0.85,0.5)(1,1.15)(1.5,1.45)(2.1,1)(2,0.3)(1.5,0)
\pscurve(5.1,0)(4.6,0.2)(4.45,0.5)(4.6,1.15)(5.1,1.45)(5.7,1)(5.6,0.3)(5.1,0)
\pscurve(1.1,0.6)(1.5,1)(1.9,0.5)(1.5,0.3)(1.1,0.6)
\pscurve(1.3,0.7)(1.5,0.9)(1.7,0.7)(1.5,0.4)(1.3,0.7)
\pscurve(4.8,0.7)(5,1.1)(5.4,0.6)(5,0.3)(4.8,0.7)
\pscurve(4.9,0.7)(5.05,1)(5.25,0.7)(5,0.5)(4.9,0.7)
\pscurve(6,0.8)(6.4,0.85)(6.75,1)(6.75,1.2)(6.3,1.3)
\pscurve(6.4,2.4)(6.3,2)(6.3,1.6)
\pscurve(0,1)(0.2,1.2)(0.8,1)
\pscircle(2.5,3.6){0.4}
\psline(2.4,3.2)(2.2,3)(1.9,2.65)
\psline(2.6,3.2)(2.8,2.7)
\psline(2.3,3.7)(2.4,3.6)
\psline(2.5,3.7)(2.6,3.6)
\psline(8.6,1.9)(8.6,0)%BD
\psdots(8.6,1.9)(8.6,0)(6.35,0)(13.9,0)(6.35,2.7)
\psline(0,0)(6.4,0)
\uput[u](8.6,1.9){B}\uput[d](8.6,0){D}
\uput[ur](6.35,2.7){A}\uput[d](6.35,0){E}
\uput[d](13.9,0){C}
\rput(14.5,3.5){Données :}
\rput(14.5,1.9){\begin{tabular}{l}
(AE) // (BD)\\ AE = 1,50 m\\ BD = 1,10 m\\ EC = 6 m
\end{tabular}}
 \end{pspicture}
\end{center} 

\begin{enumerate}
\item Calculer DC. 
\item En déduire que ED = 1,60~m. 
\item Une fillette mesure 1,10~m. Elle passe à 1,40~m derrière la camionnette. 

Le conducteur peut-il la voir ? Expliquer.
\end{enumerate}
"""
corrige = r"""
\begin{enumerate}
\item %Calculer DC.
Les droites (AE) et (BD) sont parallèles ; les points E, D, C d'une part, A, B, C de l'autre sont alignés dans cet ordre ; le théorème de Thalès permet d'écrire :

$\dfrac{\text{DC}}{\text{EC}} =  \dfrac{\text{BD}}{\text{AE}}$ soit $\dfrac{\text{DC}}{6} = \dfrac{1,1}{1,5}$ soit DC $ = 6\times \dfrac{1,1}{1,5} = 4,4$~m.
\item %En déduire que ED = 1,60~m.
On a ED = $\text{EC} - \text{DC} = 6 - 4,4 = 1,6$~m. 
\item %Une fillette mesure 1,10~m. Elle passe à 1,40~m derrière la camionnette. 

%Le conducteur peut-il la voir ? Expliquer.
Comme $1,4 < 1,6$ et que la jeune fille a pour taille BD, elle sera entièrement dans la zone grisée  : le conducteur ne la verra pas.
\end{enumerate}
"""


LesExos+= [ExoBrevet(annee, question, corrige)]


annee = "DNB Décembre 2015 Nouvelle Calédonie"

question = r"""
Un marionnettiste doit faire un spectacle sur le thème de l'ombre. Pour cela il a besoin que sa marionnette de 30~cm ait une ombre de 1,2~m.

La source de lumière C est située à 8 m de la toile (AB).

La marionnette est représentée par le segment [DE].

\medskip

\begin{enumerate}
\item Démontrer que les droites (AB) et (DE) sont parallèles.
\item Calculer EC pour savoir où il doit placer sa marionnette.
\end{enumerate}

\begin{center}
\psset{unit=1cm}
\begin{pspicture}(12,5.5)
%\psgrid
\pspolygon(0.5,1.2)(9.5,1.2)(0.5,5)
\psline(7.5,1.2)(7.5,2.05)
\psframe(0.5,1.2)(0.8,1.5)\psframe(7.5,1.2)(7.8,1.5)
\psline{<->}(0.5,0.6)(9.5,0.6)
\uput[d](5,0.6){8 m}\uput[l](0.5,3.1){1,2 m}
\uput[l](7.5,1.65){30 cm}
\uput[ul](0.5,5){A} \uput[dl](0.5,1.2){B} \uput[d](9.5,1.2){C} \uput[u](7.5,2.05){D} \uput[d](7.5,1.2){E}
\psset{unit=0.6cm}
\rput{-20}(16,1.9){\pspolygon*(0,-0.3)(0,0.3)(0.8,0.2)(2,0.2)(2,-0.2)(0.8,-0.2)} 
\end{pspicture}

Cette figure n'est pas à l'échelle.
\end{center}
"""

corrige = r"""
\begin{enumerate}
\item %Démontrer que les droites (AB) et (DE) sont parallèles.
Les droites (AB) et (DE) sont parallèles car perpendiculaires à la droite (BC).
\item %Calculer EC pour savoir où il doit placer sa marionnette.
Les droites  (AB) et (DE) sont parallèles, C, E, B d’une part, C, D et A d’autre part sont alignés dans cet ordre ; d’après le théorème de Thalès :

$\dfrac{\text{EC}}{\text{CB}} = \dfrac{\text{DE}}{\text{AB}}$, soit $\dfrac{\text{EC}}{8} = \dfrac{0,3}{1,2} = \dfrac{1}{4}$, d’où EC $ = 2$~m. 
\end{enumerate}

"""


LesExos+= [ExoBrevet(annee, question, corrige)]


annee = "DNB Décembre 2016 Amérique du sud"

question = r"""
Cristo Redentor, symbole brésilien, est une grande statue dominant la ville de Rio qui s'érige au
sommet du mont Corcovado.

Au pied du monument, Julien et Magali souhaitent mesurer la hauteur de la statue (socle
compris). Julien qui mesure 1,90~m, se place debout à quelques mètres devant la statue. Magali
place le regard au niveau du sol de telle manière qu'elle voit le sommet du Cristo (S) et celui de la tête de Julien (T) alignés; elle se situe alors à 10~m de la statue et à 50~cm de Julien.
La situation est modélisée ci-dessous par la figure qui n'est pas à l'échelle.

\begin{center}
\psset{unit=1cm}
\begin{pspicture}(-1,0)(7,6)
\psline[linewidth=1.25pt](1,1)(1,5.8)
\psline[linewidth=1.25pt](3.4,1)(3.4,2.3)
\psline[linestyle=dotted](1,1)(4.3,1)(1,5.8)
\uput[r](-0.8,4.8){Cristo}
\uput[r](-0.8,4.2){Redentor}
\psline{->}(0,4)(1,2.9)
\uput[l](2.4,1.7){Julien}
\psline{->}(2.2,1.5)(3.4,1.7)
\rput{-55}(3.9,2.){regard de Magali}
\psline[linestyle=dashed]{<->}(1,0.5)(4.3,0.5)
\uput[d](2.65,0.5){10~m}
\uput[u](1,5.8){S} \uput[d](1,1){C} \uput[l](3.4,2.4){T} \uput[d](3.4,1){J} \uput[dr](4.3,1){M} 
\end{pspicture}
\end{center}

Déterminer la hauteur SC de la statue en supposant que le monument et Julien sont
perpendiculaires au sol.

"""

corrige = r"""
Représentons de nouveau le triangle complété par  les longueurs  données dans l'énoncé.

\begin{center}
\psset{unit=1cm}
\begin{pspicture}(-1,0)(7,6)
\psline[linewidth=1.25pt](1,1)(1,5.8)
\psline[linewidth=1.25pt](3.4,1)(3.4,2.3)
\psline[linestyle=dotted](1,1)(4.3,1)(1,5.8)
%\uput[r](-0.8,4.8){Cristo}
%%\uput[r](-0.8,4.2){Redentor}
%\psline{->}(0,4)(1,2.9)
%\uput[l](2.4,1.7){Julien}
%\psline{->}(2.2,1.5)(3.4,1.7)
%\rput{-55}(3.9,2.){regard de Magali}
\psline[linestyle=dashed]{<->}(1,0.5)(3.4,0.5)
\psline[linestyle=dashed]{<->}(3.4,0.5)(4.3,0.5)
\uput[d](3.85,0.5){0,5~m}
\uput[d](2.2,0.5){9,5~m}
\uput[u](1,5.8){S} \uput[d](1,1){C} \uput[l](3.4,2.4){T} \uput[d](3.4,1){J} \uput[dr](4.3,1){M}
\uput[l](3.4,1.7){1,90~m} 
\end{pspicture}
\end{center} 

Pour déterminer la longueur de la hauteur [SC], il faut utiliser le théorème de Thalès. Cependant, avant de s'engager dans sa formulation, nous devons vérifier que les droites (SC) et (TJ) sont parallèles, condition à l'utilisation du théorème.

On sait que : (SC) et  (CM) d'une part  et (TJ) et  (CM) de l'autre sont perpendiculaires.

Or : si deux droites sont perpendiculaires à une même troisième, alors elles sont parallèles.
Donc : (SC) // (TJ).

On peut maintenant passer à l'énonciation du théorème de Thalès en réunissant toutes les conditions
nécessaires.

On sait que: S, T et M sont alignés ainsi que C, J et M. De plus, (SC) // (TJ).

Donc d'après Thalès  : $\dfrac{\text{MT}}{\text{MS}} = \dfrac{\text{MJ}}{\text{MC}} = \dfrac{\text{TJ}}{\text{SC}}$

Soit ici :  $\dfrac{\text{MT}}{\text{MS}} = \dfrac{0,5}{10} = \dfrac{1,9}{\text{SC}}$.

D'où avec les deux derniers quotients SC $= \dfrac{1,9 \times 10}{0,5} = 38$~m.

La statue mesure environ 38 mètres.

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