from pylog import *

class F(Term):
    pass

x = Var('x');
y = Var('y');

s0 = Stack();
# s1 = s0.unify(F(x, 'John'),'Bob');
try:
    s1 = s0.unify(F(Var('x'), 'John'),'Bob').next();
    # s1 = s0.unify(F(x, 'John'),F('Bob', y)).next();
    # s1 = s0.unify(F(x, 'John'),F('Bob', x)).next();
    print s1(x)
except StopIteration:
	print "can not unify"
# s1 = s0.unify(F(x, 'John'),F('Bob', y)).next();
# print s1(x)
# print s1(y)
