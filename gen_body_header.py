from cgitb import text
from utils import load_text_file


def gen_body_header(dicoargs):
    text_file = load_text_file(dicoargs["path"])
    for k in dicoargs:
        text_file = text_file.replace("{w_"+k +"}", dicoargs[k])
    return text_file