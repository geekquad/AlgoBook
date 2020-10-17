m = [[112,345,765,834],[243,234,65,987],[765,296,690,963]] 
for row in m : 
    print(row) 
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))] 
print("\n") 
for row in rez: 
    print(row) 