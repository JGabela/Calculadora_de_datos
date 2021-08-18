from decimal import Decimal

#this block determines the number of decimal the media must have
def cs(x, y, z):
    x = Decimal(x)
    y = Decimal(y)
    z = Decimal(z)
    cs.cstt = max(x.as_tuple().exponent, y.as_tuple().exponent, z.as_tuple().exponent)

def cs1(x, y, z, t):
    x = Decimal(x)
    y = Decimal(y)
    z = Decimal(z)
    t = Decimal(t)
    cs1.cs1tt = max(x.as_tuple().exponent, y.as_tuple().exponent, z.as_tuple().exponent, t.as_tuple().exponent)

def cs2(x, y, z, t, op):
    x = Decimal(x)
    y = Decimal(y)
    z = Decimal(z)
    t = Decimal(t)
    op = Decimal(op)
    cs2.cs2tt = max(x.as_tuple().exponent, y.as_tuple().exponent, z.as_tuple().exponent, t.as_tuple().exponent, op.as_tuple().exponent)

def cs3(x, y, z, t, op, io):
    x = Decimal(x)
    y = Decimal(y)
    z = Decimal(z)
    t = Decimal(t)
    op = Decimal(op)
    io = Decimal(io)
    cs3.cs3tt = max(x.as_tuple().exponent, y.as_tuple().exponent, z.as_tuple().exponent, t.as_tuple().exponent, op.as_tuple().exponent, io.as_tuple().exponent)
