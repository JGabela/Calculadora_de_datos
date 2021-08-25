
def sk(rg):
    if rg == 'si':
        sk.jmgs = True
    elif rg == 'SI':
        sk.jmgs = True
    elif rg == 'Si':
        sk.jmgs = True
    elif rg == '1':
        sk.jmgs = True
    elif rg == 'no':
        sk.jmgs = False
    elif rg == 'NO':
        sk.jmgs = False
    elif rg == 'No':
        sk.jmgs = False
    elif rg == '0':
        sk.jmgs = False
    else:
        sk.jmgs = False
