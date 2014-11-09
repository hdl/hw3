from pylog import *

class F(Term):
    pass

x = Var('x');

s0 = Stack();
s1 = s0.unify(F(x),F('r')).next();
print s1(x)
print s1(F(x))
print s1(F('r'))
