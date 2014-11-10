from pylog import *

class F(Term):
    pass
class G(Term):
    pass

x = Var('x');
y = Var('y');

s0 = Stack();
s1 = s0.unify(F(x, 'John'),'Bob');
print s1
s1 = s0.unify(F(x, 'John'),F('Bob', 'John'));
print s1(x)
s2 = s0.unify(F(x, 'John'),G('Bob', 'John'));
print s2(x)
#try:
#    s1 = s0.unify(F(Var('x'), 'John'),'Bob').next();
#    # s1 = s0.unify(F(x, 'John'),F('Bob', y)).next();
#    # s1 = s0.unify(F(x, 'John'),F('Bob', x)).next();
#    print s1(x)
#except StopIteration:
#	print "can not unify"
# s1 = s0.unify(F(x, 'John'),F('Bob', y)).next();
# print s1(x)
# print s1(y)
