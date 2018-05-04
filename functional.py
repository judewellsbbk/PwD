def negate(f):
    """return a function that for any input x returns -f(x)"""

    return lambda *args, **kwargs: -f(*args, **kwargs)

def myincrementor(n):
    return n+1

g =  negate(myincrementor) # g is a new function

print g(6)