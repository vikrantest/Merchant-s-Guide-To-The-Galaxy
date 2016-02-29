digits = {
    "i": 1,
    "v": 5,
    "x": 10,
    "l": 50,
    "c": 100,
    "d": 500,
    "m": 1000
}


input = ['glob is I',
'prok is V',
'pish is X',
'tegj is L',
'glob pish Silver is 30 Credits',
'glob prok Gold is 57800 Credits',
'pish pish Iron is 3910 Credits',
'how much is pish tegj glob glob glob ?',
'how many Credits is pish glob Silver ?',
'how many Credits is glob glob prok Gold ?',
'how many Credits is glob glob prok Iron ?',
 'how much wood could a woodchuck chuck if a woodchuck could chuck wood ?'
]

scrap_metal=[]
non_repeat_symbol = ['dd+','ll+','vv+']
triple_repeat_symbol = ['iiii+','cccc+','xxxx+','mmmm+',]
non_subtracted_symbol = ['d','l','v']
quad_repeating_symbol = ['i','x','c','m']
difference_dict = {
        "i":"vx",
        "x":"lc",
        "c":"dm"
        }

symbol_value = {}

digit_symbol={}

comodity_value = {}
temp_dict={}
output=[]


