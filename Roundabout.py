from decimal import Decimal

def count_sigfigs(numstr):
    numstr = Decimal(numstr)
    count_sigfigs.rer = abs(numstr.as_tuple().exponent)
