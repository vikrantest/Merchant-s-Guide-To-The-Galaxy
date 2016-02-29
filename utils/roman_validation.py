from utils import *
import re
from collections import Counter

def multiple_repeat_validation(string_num,counts):
        roman=True
        for sym,count in counts.items():
                if count == 4:
                        
                        val = sym+''+sym+''+sym
                        result_list = string_num.split(val)
                        try:
                                result_list = result_list[1].split(sym)
                                if len(result_list[0])==1:
                                        if digits[result_list[0]] > digits[sym]:
                                                roman = False
                                                return roman
                                        else:
                                                roman=True
                                else:roman=False
                        except:roman=True
                elif count >4:
                        roman=False
                        return False
                                
                else:roman=True
        return roman
                

class RomanValidation():
        def repeatation_validation(self,roman_number):
                roman=True
                for num in roman_number:
                        try:
                                temp_dict[digit_symbol[num]]=0
                        except:
                                return False
                list_num = [digit_symbol[x] for x in roman_number]
                string_num = ''.join(list_num)
                for pattern in non_repeat_symbol:
                        match = re.search(pattern,string_num)
                        if match:
                                roman=False
                                return roman
                for pattern in triple_repeat_symbol:
                        match = re.search(pattern,string_num)
                        if match:
                                roman=False
                                return roman
                counts = Counter(string_num)
                if 4 in counts.values():
                        roman = multiple_repeat_validation(string_num,counts)
                                        
                return roman

        def subtract_validation(self,roman_number1,roman_number2):
                roman = True
                if roman_number2 in non_subtracted_symbol:
                        roman=False
                        return roman

                elif roman_number2 == 'i' and roman_number1 not in difference_dict[roman_number2]:
                        roman=False
                        return roman

                elif roman_number2 == 'x' and roman_number1 not in difference_dict[roman_number2]:
                        roman=False
                        return roman
                
                elif roman_number2 == 'c' and roman_number1 not in difference_dict[roman_number2]:
                        roman=False
                        return roman

                else:return roman

        
                
                
                
        
