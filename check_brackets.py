# check given sting has a valide brackets open and close and in correct way
strr = "{[]}<>"

dt ={"(":")","{":"}","[":"]","<":">"}
st = ""
for i in strr:
    if i in dt.keys() or i in dt.values():
        st = st + i
flag = ""
j = 0
while (j <= len(st)):
    if st == "":
        flag = True
        break
    if len(st) % 2 != 0:
        flag = False
        break    
    if (j <= len(st) - 2 and st[j] in dt.keys()) and st[j+1] in dt.keys():
        j = j+1
        continue
    elif len(st) == 2 and st[1] in dt.keys() and st[2] == dt[st[1]]:
        st = ""
        flag = True
        break
    elif(j <= len(st) - 2  and st[j] in dt.keys() and st[j+1] == dt[st[j]]):
        st = st.replace(st[j+1],"")
        st = st.replace(st[j],"")
        j += 1
    else:
        flag = False
        break    
    j = 0
print("result",flag)
