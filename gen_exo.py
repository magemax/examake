
# class Exo
from utils import appeler_fonction_dans_fichier, charger_fichiers_yaml



class Exo:
    def __init__(self, dico_from_yaml):
        self.id= dico_from_yaml["id"]
        self.nom= dico_from_yaml["nom"]
        self.tags = dico_from_yaml["tags"]
        self.headers = set(dico_from_yaml["headers_needed"])
        self.body = dico_from_yaml["body"]
        self.source= dico_from_yaml
        self.builder = appeler_fonction_dans_fichier("./body_builders/"+ self.body["script"], self.body["script"].split(".")[0], "build")
        print("builder", self.builder)
    def build(self):
        print(self.body)
        return self.builder(**(self.body["arguments"]))



dossier_exercices = "./Exercices"  # Remplacez cela par le chemin de votre dossier
print("Loading Exercices list")
EXERCICES = {exo["id"]: Exo(exo) for exo in charger_fichiers_yaml(dossier_exercices)}


# Maintenant, resultats contient une liste des fichiers YAML chargés
# Vous pouvez les traiter comme des dictionnaires Python
for fichier_yaml in EXERCICES:
    print(f"Fichier YAML chargé : {fichier_yaml}, {EXERCICES[fichier_yaml]}")

def gen_exercice(id_exercice):
    exercice= EXERCICES[id_exercice]
    return exercice


if __name__ == "__main__":
    print(gen_exercice("lettre_fonction"))
