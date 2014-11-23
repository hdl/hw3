class Predictor:
    """ Base class for KB table raw
    """

    def __init__(self, name, line):
        self.predict_name = name
        self.positive_list = []
        self.conclusion_dict= {}
        if '=>' in line:
            self.add_as_conclusion(line)
        else:
            self.add_as_positive(line)

    def __str__(self):
        name = 'predict_name:'+ self.predict_name+'\n'
        positive = 'postive_list:'+str(self.positive_list)+'\n'
        conclusion = 'conclusion_dict:'+str(self.conclusion_dict)+'\n'
        return name+positive+conclusion

    def add_as_conclusion(self,expression):
        if "=>" in expression:
            premise_con = expression.split('=>')
            key = premise_con[-1]
            value = premise_con[0].split('&')
            if key in self.conclusion_dict:
                self.conclusion_dict[key].append(value)
            else:
                self.conclusion_dict[key] = []
                self.conclusion_dict[key].append(value)
        else:
            print "error, should include =>"
            print expression
            traceback.print_stack()

    def add_as_positive(self,expression):
        if "=>" not in expression:
            if "&" in expression:
                print "error, should not include &"
                print expression
                traceback.print_stack()
            self.positive_list.append(expression)
        else:
            print "error, should not include =>"
            print expression
            traceback.print_stack()




