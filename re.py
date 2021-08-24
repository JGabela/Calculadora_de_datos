
def rer(vrr):
    if vrr == 'si':
        rer.vrr = True
    elif vrr == 'SI':
        rer.vrr = True
    elif vrr == 'Si':
        rer.vrr = True
    elif vrr == '1':
        rer.vrr = True
    elif vrr == 'no':
        rer.vrr = False
    elif vrr == 'NO':
        rer.vrr = False
    elif vrr == 'No':
        rer.vr = False
    elif vrr == '0':
        rer.vrr = False
