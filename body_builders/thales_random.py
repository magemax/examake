import body_builders.thales_normal
import body_builders.thales_indirect
from random import choice

def build(**args): 
    tochoose=choice([body_builders.thales_normal.build, body_builders.thales_indirect.build])
    return tochoose(**args)