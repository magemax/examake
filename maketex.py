from fileinput import filename
from utils import latex_compile
from interro_builder import build_interro
import os
from datetime import datetime

interro_name="ds_troisieme_probas"#"ds_troisieme_probas"
import random


random.seed(13)

filename=f'{datetime.now().strftime("%Y%m%dT%H%M%S")}_' + interro_name
pathname=f"Outputs/{filename}/"

contenu=build_interro(interro_name)
if not os.path.exists(pathname):
    os.mkdir(pathname)


def exporter_texte_vers_fichier(texte, nom_fichier):
    try:
        with open(nom_fichier, 'w', encoding='utf-8') as fichier:
            fichier.write(texte)
        print(f"Le texte a été exporté dans '{nom_fichier}' avec succès.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'exportation du texte dans '{nom_fichier}': {str(e)}")
        raise


exporter_texte_vers_fichier(contenu, pathname+"Interro.tex")
latex_compile(pathname+"Interro.tex", "Sujet.pdf", pathname)

contenu_corrige=contenu.replace(r"\setboolean{correction}{false}", r"\setboolean{correction}{true}")
exporter_texte_vers_fichier(contenu_corrige, pathname+"Corrige.tex")
latex_compile(pathname+"Corrige.tex", "Corrige.pdf", pathname)