from predictor import *
class Term:
    def __init__(self, term_string):
        self.predict_name = self.get_predict_name(term_string)
        self.member_list = term_string.replace(self.predict_name+"(", "")[:-1].split(',')

    def get_predict_name(self,line):
        if "=>" in line:
            conclusion = line.split('=>');
            return conclusion[-1].split('(')[0]
        else:
            return line.split('(')[0]


class KB(Term):
    """ Base class for KB key:value table
    """

    def __init__(self):
        self.table = {}

    def print_info(self):
        for key, value in self.table.iteritems():
            print "key is:"+str(key)
            print value

    def tell_as_conclusion(self,line):
        predict_name = self.get_predict_name(line)
        if predict_name in self.table:
            self.table[predict_name].add_as_conclusion(line)
        else:
            predict_obj = Predictor(predict_name, line)
            self.table[predict_name] = predict_obj

    def tell_as_positive(self,line):
        predict_name = self.get_predict_name(line)
        if predict_name in self.table:
            self.table[predict_name].add_as_positive(line)
        else:
            predict_obj = Predictor(predict_name, line)
            self.table[predict_name] = predict_obj

    def ask(self, goal):
        goal_predict = self.get_predict_name(goal)
        if goal_predict not in self.table:
            return False
        elif self.check_positive_list(goal):
            return True
        elif self.check_conclusion_dict(goal):
            return True
        else:
            return False

    def check_positive_list(self, goal):
        key = self.get_predict_name(goal)
        for item in self.table[key].positive_list:
            if goal==item:
                return True
            elif self.unify(goal, item) != False:
                return True
        return False

    def check_conclusion_dict(self, goal):
        return False

    def unify(self, term_string1, term_string2):
        term1 = Term(term_string1)
        term2 = Term(term_string2)
        if term1.predict_name != term2.predict_name:
            return False
        elif len(term1.member_list) != len(term2.member_list):
            return False
        else:
            return self._unify(term1.member_list, term2.member_list, '')

    def _unify(self, list1, list2, theta):
        print str(list1)+" "+str(list2)
        if str(list1)==str(list2):
            return theta 
        for foo, bar in zip(list1, list2):
            if foo != bar:
                break
        if foo == 'x':
            self.subst(list1,bar)
            self.subst(list2,bar)
            return self._unify(list1,list2,bar)
        elif bar == 'x':
            self.subst(list1,foo)
            self.subst(list2,foo)
            return self._unify(list1,list2,foo)
        else:
            return False

    def subst(self, foo_list, foo):
        for i in range(len(foo_list)):
            if foo_list[i] == 'x':
                foo_list[i] = foo


