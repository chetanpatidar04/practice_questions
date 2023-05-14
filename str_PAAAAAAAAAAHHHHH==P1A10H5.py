# program to input == str_PAAAAAAAAAAHHHHH o/p = P1A10H5
# first method
string  = "PAAAAAAAAAAHHHHH"
char = ""
count = 1
st = ""
# for i in string:
#     count = string.count(i)
#     if i not in st:
#         st = st + i + str(count)
# print(st)
from collections import OrderedDict
di = OrderedDict()
# second method
for i in range(0,len(string)):
    if string[i] == char:
        count = count + 1    
    else:
        count = 1
        char = string[i]
    di[char] = count
for key, value in di.items():
    st = st + key + str(value)
print(st)