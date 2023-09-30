from utils import charger_fichiers_yaml,load_text_file
from gen_body_header import gen_body_header
from gen_exo import gen_exercice

class Exam:
    def __init__(self, dico_from_yaml):
        self.nom=dico_from_yaml["nom"]
        self.id=dico_from_yaml["id"]
        self.nombre_genere=dico_from_yaml["nombre_genere"]
        self.source=dico_from_yaml
        self.base_headers=[] if "headers" not in dico_from_yaml else dico_from_yaml["headers"]
    def activate(self):
        dico_from_yaml=self.source
        self.template=load_text_file(dico_from_yaml["template_body"])
        self.body_headers=[gen_body_header(h) for h in dico_from_yaml["body_headers"]]
        self.exercices= [gen_exercice(k) for k in dico_from_yaml["exercices"]]

dossier_interros = "./interros"  # Remplacez cela par le chemin de votre dossier
print("Loading Exercices list")
EXAMS = {interro["id"]: Exam(interro) for interro in charger_fichiers_yaml(dossier_interros)}


def import_headers(hds):
    headers=[]
    for h in hds:
        headers+=[load_text_file("assets/headers/"+ h+ ".tex")]
    return headers

def build_interro(nom):
    if nom not in EXAMS:
        print("No such interro id specified in the interros files")
        print(EXAMS, nom)
        raise
    interro = EXAMS[nom]
    interro.activate()
    all_headers=set(interro.base_headers)
    for exo in interro.exercices:
        all_headers|=exo.headers
    txt_headers = import_headers(all_headers)

    #load le fichier texte
    main_file=interro.template
    #insère les headers nécessaires aux différents exos
    main_file=main_file.replace("{w_headers}", ("\n".join(txt_headers)))
    #print(main_file)
    #input()

    fichiers=[]
    
    for _ in range(interro.nombre_genere):
        txt=interro.body_headers[:]
        for k in interro.exercices:
            txt+=[k.build()]
        fichiers+=["\n\\vspace{0.5 cm}\n".join(txt)]
    main_file= main_file.replace("{w_body}", "\n\n \\newpage \n\n".join(fichiers))
    return main_file
