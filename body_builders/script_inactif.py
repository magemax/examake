from template_management import load_template


def build(**args): 
    texte_individuel=load_template(args["template"])
    dico = {}

    for k,v in dico.items():
        texte_individuel=texte_individuel.replace("{w_"+k+"}",str(v))
        
    return(texte_individuel)