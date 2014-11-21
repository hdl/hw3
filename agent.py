from predictor import *
from KB import *
import sys, traceback

def main():
    kb = KB()

    f = open('input.txt', 'r')
    print f.read()
    f.close()
    print "===================================="

    f = open('input.txt', 'r')
    goal = f.readline().translate(None, "\n\r\t");
    num = int(f.readline().translate(None, "\n\r\t"));
    for i in range(num):
        line = f.readline().translate(None, "\n\r\t");
        if '=>' in line:
            kb.tell_as_conclusion(line)
        elif '&' in line:
            line_list = line.split('&');
            for new_line in line_list:
                kb.tell_as_positive(new_line)
        else:
            kb.tell_as_positive(line)
    f.close();

    kb.print_info()
    
    output_str = str(kb.ask(goal)).upper()
    print output_str
    f = open('output.txt', 'wr')
    f.write(output_str)
    f.close()


if __name__ == '__main__':
    main()



