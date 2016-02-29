from utils import *
import re
from collections import Counter
from roman_validation import *
from process import *


class GalacticProcess():

        def input_process(self):
                answer = raw_input('If you want to give your own input enter "Y" else "N" -->  ')

                if 'Y' in answer:
                        no_of_lines = raw_input("How many lines of input you want to enter?")
                        try:
                                no_of_lines = int(no_of_lines)
                                for x in range(1,no_of_lines+1):
                                        lines = raw_input("Enter you input here - :")
                                        self.main_method(lines)

                        except:
                                output.append("Please enter a number not a string")
                else:        
                        for x_line in input:
                                self.main_method(x_line)
                if len(output) == 0:
                        print "Please enter correct input in order to get some output....check some reference for roman numbers"
                for outs in output:
                        print outs


        def main_method(self,lines):
                lines = lines.lower().split(None)
                process_values = ProcessInputLines()
                if len(lines) == 3:
                        process_values.process_value_assign(lines)
                elif len(lines)>4 and 'credit' in lines[-1] and 'is' in lines[-3]:
                        process_values.process_metal_value(lines)
                elif len(lines)>4 and '?' in lines[-1]:
                        if lines[-2] in symbol_value.keys() or lines[-2] in comodity_value.keys() or lines[-2] in scrap_metal:
                                
                                if not lines[-2] in scrap_metal:
                                        if lines[-2] in comodity_value.keys():
                                                metal=True
                                        else:
                                                metal=False
                                        if metal:process_values.calculate_metal_value(lines)
                                        else:process_values.calculate_roman_value(lines)
                        else:
                                output.append("I have no idea what you are talking about , We don't have these metals ")
                                        

if __name__ == '__main__':
        GalacticProcess().input_process()
        



