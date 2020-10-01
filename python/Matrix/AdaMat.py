#AdaMatrix- codechef September Long challenge  Problem  Solution
#By Abhinav Yadav


a=int(input())   #input for no. of test cases
while(a>0):
    b=int(input())  #size of squarematrix
    l=[]   #creating an empty list
    for i in range(0,b):
        # taking input matrix and appending each row in list l
        l.append(list(map(int,input().split(" "))))  
    i=1
    u=0 #counter for counting the output
    j=-1 #initially marking element is not present at it;s right position
    while (i < b): #iterating in first row of the  list
        # if element and it's position is not equal(if element is not at it's right position)
        if ((l[0][i]) != (i + 1)): 
            if (j == 1):#if previous element of  current element was at it's right position
                u = u + 2
            elif (i == (b - 1)): #boundary condition
                if (j != 1 and u == 0):
                    u = u + 1
            elif ((i + 1) < b):
                if ((l[0][i + 1]) == (i + 2) and u == 0): 
                    u = u + 1

            j = - 1  #mark current element was not at it's right position

        else:
            j = 1   #mark current element was  at it's right position
        i = i + 1
    print(u) #printing output for each test case
    a = a - 1


