import os
from string import ascii_uppercase




def ff():
    
    for i in ascii_uppercase:
        fp = f"{i}.txt"
        with open(fp, 'x'):
            pass

ff()