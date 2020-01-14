import numpy as np
localefile="locale/en_US.txt"
def lang(line, script):
    mylines = []
    mylines = np.loadtxt(localefile, comments="#", delimiter=";", unpack=False, dtype=str)
    if script == 1:
        n=eval(mylines[line])
        return(n)
    else:
        return(mylines[line])