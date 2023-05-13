# program to print  given string = P1A10H5  o/p = PAAAAAAAAAAHHHHH

string = "P1A10H5"
digi = ""
cha = ""
st = ""
for i in range (0, len(string)):
    if string[i].isdigit():
        digi = digi + string[i]
    else:
        digi = ""
        cha = string[i]
    if digi != "":
        st = st + (cha * int(digi))
print(st)