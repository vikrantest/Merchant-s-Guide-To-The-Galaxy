from utils import *
import re
from collections import Counter
from roman_validation import *


def process_roman_number(line):
        #line = l.lower().split(None)
        length_line = len(line)
        validation = RomanValidation()
        string_gal=' '.join(line)
        roman_validation = validation.repeatation_validation(line)
        if not roman_validation:
                output.append("( "+string_gal+") Please check your line , It's invalid galactic number")
                return False
        result_value=0
        for val in range(0,length_line):
                if '0' not in line[val] and val+1<length_line:
                        if symbol_value[line[val]] < symbol_value[line[val+1]] and val < length_line:
                                roman_note = validation.subtract_validation(digit_symbol[line[val+1]],digit_symbol[line[val]])
                                if not roman_note:
                                        output.append("( "+string_gal+") Please check your line , It's invalid galactic number")
                                        return False
                                result_value += symbol_value[line[val+1]] - symbol_value[line[val]]
                                line[val]='0'
                                line[val+1]='0'
                               
                        else:
                                result_value+=symbol_value[line[val]]
                elif val+1 >= length_line and '0' not in line[val]:
                        result_value+=symbol_value[line[val]]

        return result_value
        
             
#print process_roman_number('pish tegj glob glob')
class ProcessInputLines():
        def process_value_assign(self,line):
                if line[2] not in digits.keys():
                        output.append("It is not a valid roman number")
                else:
                        digit_symbol[line[0]] = line[2]
                        symbol_value[line[0]]=digits[line[2]]
        def process_metal_value(self,line):
                line.pop()
                try:
                        value = float(line[-1])
                except:
                        output.append("'%s' is not a valid numeric value" % line[-1])
                line.pop()
                line.pop()
                metal = line.pop()
                total_value = process_roman_number(line)
                if total_value:comodity_value[metal]=value/total_value
                else:scrap_metal.append(metal)
                

        def calculate_metal_value(self,line):
                line.pop()
                metal = line.pop()
                galactic_list=[]
                while line:
                        val=line.pop()
                        if val != 'is':
                                galactic_list.append(val)
                        else:break
                galactic_list=galactic_list[::-1]
                string_result = ' '.join(galactic_list)
                total_value = process_roman_number(galactic_list)
                final_credits = comodity_value[metal]*total_value
                output.append(string_result+' '+metal+' is '+str(final_credits)+' credits')


        def calculate_roman_value(self,line):
                line.pop()
                galactic_list=[]
                while line:
                        val=line.pop()
                        if val != 'is':
                                galactic_list.append(val)
                        else:break
                galactic_list=galactic_list[::-1]
                string_result = ' '.join(galactic_list)
                total_value = process_roman_number(galactic_list)
                output.append(string_result+' is '+str(total_value))
  
                

                


