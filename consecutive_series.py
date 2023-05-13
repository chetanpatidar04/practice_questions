string  = [0,12,4,5,22,34,6]
counter = 1
string.sort()
li=[]
for i in range(len(string)):
 if i <= len(string) - 2 and string[i]+1 == string[i+1]:
  counter += 1
 else:
  li.append(counter)
  counter = 1
li.sort()    
print(li[-1])