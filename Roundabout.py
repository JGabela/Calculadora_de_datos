from decimal import Decimal

def count_sigfigs(numstr):

    count_sigfigs.rer = len(Decimal(numstr).normalize().as_tuple().digits)
