
import os
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
import yaml
import importlib.util
import subprocess

def appeler_fonction_dans_fichier(chemin_fichier, nom_module, nom_fonction):
    try:
        # Charger le module à partir du chemin du fichier
        spec = importlib.util.spec_from_file_location(nom_module, chemin_fichier)
        print("spec", spec)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Appeler la fonction du module avec les arguments fournis
        fonction = getattr(module, nom_fonction)
        return fonction
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")
        raise


def charger_fichiers_yaml(dossier):
    fichiers_yaml = []
    for dossier_racine, sous_dossiers, fichiers in os.walk(dossier):
        for fichier in fichiers:
            if fichier.endswith(".yaml") or fichier.endswith(".yml"):
                chemin_fichier = os.path.join(dossier_racine, fichier)
                with open(chemin_fichier, 'r', encoding='utf-8') as fichier_yaml:
                    contenu_yaml = yaml.load(fichier_yaml, Loader=yaml.FullLoader)
                    if contenu_yaml["id"] in fichiers_yaml:
                        print("Duplicate key, error :", fichier_yaml[contenu_yaml["id"]], contenu_yaml)
                        raise
                    fichiers_yaml+=[contenu_yaml]
    return fichiers_yaml

def load_text_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
        return contenu
    except FileNotFoundError:
        print(f"Le fichier '{path}' n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")
    raise

import subprocess

def latex_compile(tex_file, output_filename=None, output_folder=None, mode="rubber"):
    if mode=="pdflatex":
        command=["pdflatex"]
        command+=[tex_file]
        command+=[f"-aux-directory=./Outputs/intfiles"]
        if output_folder is not None:
            command+=[f"-output-directory=./{output_folder}"]
        print("Command to run", " ".join(command))
        process=subprocess.Popen(" ".join(command), shell=True)
        stdout, stderr = process.communicate()

    elif mode=="rubber":
        command=["rubber -d"]
        if output_folder is not None:
            command+=[f"--into {output_folder}"]
        if output_filename is not None:
            command+=[f"--jobname {output_filename[:-4]}"]
        command+=[tex_file]

        print("Command to run", " ".join(command))
        process=subprocess.Popen(" ".join(command), shell=True)
        stdout, stderr = process.communicate()
    else:
        raise