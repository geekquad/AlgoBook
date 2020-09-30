#Cocktail Shaker Sort

#This is a variation of Bubble Sort
#Cocktail sort traverses through a given array in both
#directions alternatively

def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n-1
    while (swapped==True):

        #rest swap =False
        #because it might be true from the
        #previous iteration
        swapped = False

        for i in range (start, end): #loop similar to bubble sort
            if (a[i] > a[i+1]) :
                a[i], a[i+1]= a[i+1], a[i]
                swapped=True

        #no change , then array is already sorted
        if(swapped ==False):
                 break

        #otherwise reset sp that it can be used in next stage
        swapped = False

        #move end point back by one
        #because
        #item at the end is in its rightful spot
        end= end-1

        #now, since cocktail shaker traverses from both sides so,
        #from right to left doing the same
        #comparision similar to the previous stage
        for i in range(end-1, start-1,-1):
            if (a[i] > a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        #increasing starting point
        #so, the last stage will move the next
        #smallest number
        start = start+1


#Main/Driver Code
a = []
n = int(input("Enter no of elements:"))
for i in range(0,n):
    element = int(input())
    a.append(element)

cocktailSort(a)
print("Sorted array is:")
for i in range(len(a)):
    print ("%d" %a[i]),
