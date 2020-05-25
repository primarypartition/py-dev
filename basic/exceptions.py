############################
### exceptions
############################


try:
    f = open('testfile','w')
    f.write('Test write this')
except IOError:
    print("Error: Could not find file or read data")
except:
    print("Error: Could not find file or read data")
finally:
   print("Always execute finally code blocks")
else:
    print("Content written successfully")
    f.close()
   
   
############################
### regular expressions
############################   


import re

re.search(pattern,  text)

match = re.search(pattern,  text)

type(match)

match.start()

match.end()

split_term = '@'

re.split(split_term,phrase)

re.findall('match','test phrase match is in middle')

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = [ 'sd*',          # s followed by zero or more d's
                  'sd+',          # s followed by one or more d's
                  'sd?',          # s followed by zero or one d's
                  'sd{3}',        # s followed by three d's
                  'sd{2,3}',      # s followed by two to three d's
                  '[sd]',         # either s or d
                  's[sd]+',       # s followed by one or more s or d
                  '[^!.? ]+',     # exclude
                  '[a-z]+',       # sequences of lower case letters
                  '[A-Z]+',       # sequences of upper case letters
                  '[a-zA-Z]+',    # sequences of lower or upper case letters
                  '[A-Z][a-z]+',  # one upper case letter followed by lower case letters    
                  r'\d+',         # sequence of digits
                  r'\D+',         # sequence of non-digits
                  r'\s+',         # sequence of whitespace
                  r'\S+',         # sequence of non-whitespace
                  r'\w+',         # alphanumeric characters
                  r'\W+',         # non-alphanumeric                  
                ]

multi_re_find(test_patterns,test_phrase)


############################
### modules
############################   


import mymodule
mymodule.func_in_mymodule()

import mymodule as mm
mm.func_in_mymodule()

from mymodule import func_in_mymodule
func_in_mymodule()

from mymodule import *
func_in_mymodule()
