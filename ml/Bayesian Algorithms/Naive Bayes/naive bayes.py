import pandas as pd
    
def custom_print(text1,text2,p):
    print('P(',text1,'="',text2,'" | buys_computer="yes")=',p[0],sep="")
    print('P(',text1,'="',text2,'" | buys_computer="no")=',p[1],sep="")
    print()
    
def single_print(text,p):
    print('P(',text,'buys_computer="yes")=',p[0],sep="")
    print('P(',text,'buys_computer="no")=',p[1],sep="")
    print()
    
def p_calc(f,total1,total2):
    return [f['yes']/total1,f['no']/total2]
    
    
data = [['<=30','high','no','fair','no'],
        ['<=30','high','no','excellent','no'],
        ['31-40','high','no','fair','yes'],
        ['>40','medium','no','fair','yes'],
        ['>40','low','yes','fair','yes'],
        ['>40','low','yes','excellent','no'],
        ['31-40','low','yes','excellent','yes'],
        ['<=30','medium','no','fair','no'],
        ['<=30','low','yes','fair','yes'],
        ['>40','medium','yes','fair','yes'],
        ['<=30','medium','yes','excellent','yes'],
        ['31-40','medium','no','excellent','yes'],
        ['31-40','high','yes','fair','yes'],
        ['>40','medium','no','excellent','no']]
headers=['Age','Income','Student','Credit Rating','Computer Bought']
df = pd.DataFrame(data, columns = headers)
print(df)
f=[{'yes':0,'no':0},{'yes':0,'no':0},{'yes':0,'no':0},{'yes':0,'no':0},{'yes':0,'no':0}] 
x=input('Enter tuple(age,income,student,credit rating) to be classified: ').split()

for i in range(14):
    f[0][df.iloc[i]['Computer Bought']]+=1
    for j in range(4):
        if df.iloc[i][headers[j]]==x[j]:
            f[j+1][df.iloc[i]['Computer Bought']]+=1

p=[p_calc(f[0],14,14)]
# buyscomputer,age,income,student,cr
for i in range(4):
    p.append(p_calc(f[i+1],f[0]['yes'],f[0]['no']))

single_print("",p[0])
p_xci=[1,1]
for i in range(4):
    custom_print(headers[i], x[i], p[i+1])
    p_xci[0]*=p[i][0]
    p_xci[1]*=p[i][1]

single_print("X | ",p_xci)

p_xci_ci=[p_xci[0]*p[0][0],p_xci[1]*p[0][1]]

print('P(X | buys_computer="yes") * P(buys_computer="yes")=',p_xci_ci[0],sep="")
print('P(X | buys_computer="no") * P(buys_computer="no")=',p_xci_ci[1],sep="")

if p_xci_ci[0]>p_xci_ci[1]:
    print('\nX belongs to class: buys_computer="yes"')
else:
    print('\nX belongs to class: buys_computer="no"')
