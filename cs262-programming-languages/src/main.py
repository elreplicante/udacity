'''
Created on 22/04/2012

@author: repli
'''

import re

def myfirst_yoursecond(p,q):
    return p[:p.find(" ")] == q[q.find(" ") + 1:]
        

#print myfirst_yoursecond("bell hooks", "curer bell")


#print re.findall(r"[a-m]", "El perro de San Roque no tiene rabo porque Ramon Ramirez se lo ha cortado")

#print re.findall(r"[0-9][ ][0-9]+","a1 2b cc3 44d")


# Assign to the variable regexp a regular expression that matches either the
# exact string ab or one or more digits.

regexp = r"ab|[0-9]+"

# regexp matches:

#print re.findall(regexp,"ab") == ["ab"]
#>>> True

#print re.findall(regexp,"1") == ["1"]
#>>> True

#print re.findall(regexp,"123") == ["123"]
#>>> True


# regexp does not match:

#print re.findall(regexp,"a") != ["a"]
#>>> True

#print re.findall(regexp,"abc") != ["abc"]
#>>> True

#print re.findall(regexp,"abc123") != ["abc123"]
#>>> True

# Assign to the variable regexp a Python regular expression that matches
# lowercase words (a-z) or singly-hyphenated lowercase words.

# Hint: It may not be possible to get correctly - do your best!

regexp = r"[a-z]+-?[a-z]+"


# regexp matches:

#print re.findall(regexp,"well-liked") == ["well-liked"]
#>>> True

#print re.findall(regexp,"html") == ["html"]
#>>> True


# regexp does not match:

#print re.findall(regexp,"a-b-c") != ["a-b-c"]
#>>> True

# RE Challenges

# Assign to the variable regexp a Python regular expression that matches single-
# argument mathematical functions.

# The function name is a lowercase word (a-z), the function argument must be a
# number (0-9), and there may optionally be spaces before and/or after the
# argument.

# Hint: You may need to escape the ( and ).



regexp = r"[a-z]+\(?[ ]*[0-9]?[ ]*\)"

# regexp matches:

#print re.findall(regexp,"cos(0)") == ["cos(0)"]
#>>> True

#print re.findall(regexp,"sqrt(   2     )") == ["sqrt(   2     )"]
#>>> True


# regexp does not match:

#print re.findall(regexp,"cos     (0)") != ["cos     (0)"]
#>>> True

#print re.findall(regexp,"sqrt(x)") != ["sqrt(x)"]
#>>> True


# Tricky REs with ^ and \

# Assign to regexp a regular expression for double-quoted string literals that
# allows for escaped double quotes.

# Hint: Escape " and \
# Hint: (?: (?: ) )

regexp = r'"(?:[^\)]|(?:\\.))*"'

# regexp matches:

#print re.findall(regexp,'"I say, \\"hello.\\""') == ['"I say, \\"hello.\\""']
#>>> True


# regexp does not match:

#print re.findall(regexp,'"\\"') != ['"\\"']
#>>> True

edges = {(1, 'a') : 2,
         (2, 'a') : 2,
         (2, '1') : 3,
         (3, '1') : 3 }

accepting = [3]

def fsmsim(string,current,edges,accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        #is there an outgoing edge?
        if(current, letter) in edges:
            destination = edges[(current,letter)]
            remaining_string = string[1:]
            return fsmsim(remaining_string, destination, edges, accepting)
        else:
            #fall of the fsm
            return False
        

print fsmsim("aaa111",1,edges,accepting)
# >>> True

        