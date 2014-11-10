from predictor import *
class KB:
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
    
    def get_predict_name(self,line):
        if "=>" in line:
            conclusion = line.split('=>');
            return conclusion[-1].split('(')[0]
        else:
            return line.split('(')[0]



