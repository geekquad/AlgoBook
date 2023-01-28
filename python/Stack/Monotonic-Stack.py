"""
Next Greater Element

Given an array of integers . Our goal is to  return an answer array which contains 
Next greater element of every elements in an array. if an element don't have any greater 
element. we add -1. 

Examples:

numbers = [ 4, 12, 5, 31, 2, 5]
answer = [ 12, 31, 31, -1, 5, -1]

Explanation:

First element in numbers array is 4  -  for 4 next greater element is 12 . the very next index itself so in answer array 
                                       we add 12 .

Next element in numbers array is 12 -  for 12 , the next element 5 is not greater than 12 so we move the next index 
                                       5 is also not greater so we move, 31 is greater.so we add 31 in the answer array.
                                       
Next element in numbers array is 5  -  for 5, 31 is next greater element. so add 31 to answer array
                      

Next element in numbers array is 31 -  for 31 , there is no greater element , so we add -1

Next element in numbers array is 2  -  for 2 , 5 is a greater element , so we add 5.

Next element in numbers array is 5  -  5 is the last element, so there is no possibility of next greater element so we add -1




How do We approach this problem?

Brute Force approcah:
      In Brute Force approach we can make 2 for loops. for every element we have to check any other element comes
      after the element is greater or not . if greater we can add the element and break the loop
      But this approach takes time complexity of O(N^2) . Can we optimise it?
 
 Of course we can use Montonic Stack.Don't Worry I wil tell you ,What is Monotonic Stack?
 
 Montonic Stack is a stack which stores the value either in an increasing order or decreasing order.
 
 Montonic Stack Approach:
 
        We are going to use montonic stack of increasing order.
        
        step 1 : First we are going to create  one empty montonic_stack . we used
                 python list but we are going to add montonic functionalityto it. Don't be panic, that's very easy we will learn that at the go.
        
        step 2 : next create an answer array and the size of answer array should be equal to given array . 
        
        step 3 :  Traverse the given array in a reverse order .
        
        step 4 :  First we  have to check monotonic stack has elements. if it have, we are going to check the last element in 
                  monotonic stack is lesser than or equal to the element from given array . if the last value in montonic stack 
                  is lesser or equal we are going to pop those values. Basically we are trying to remove all lesser values in 
                  Monotonic stack. Beacause we only want the greater elements
                 
                  
        step 5 :  After this operation if a montonic stack is empty .In answer array, in the index of traversed element we are going to put -1. beacuse there is 
                  no Greater element on the monotonic stack . if its not empty add the last value in monotonic stack to the respective position in answer
                  array because that is the larger value then our given number.
                  
        step 6 :  add  this traversed  element from given array to monotonic stack.
        
        step 7 :  Repeat step 4, 5 and 6 until we reach the first the element of given array.
         
            
 
 Time complexity : O(N)
 space Complexity: o(N)
 
        

"""

def next_greater(numbers):
    monotonic_stack = []
    # intially fill the answer array with any value with  length of an given array
    answer = [0 for i in range(len(numbers))]

    # Traverse the given array in reverse order
    for i in range(len(numbers)-1, -1, -1):

        # condition to remove all the lesser values in  montonic stack
        while monotonic_stack and monotonic_stack[-1] <= numbers[i]:
            monotonic_stack.pop()

        # after removing all the lesser values if montonic stack is empty add -1 in the position of an element in answer array
        if monotonic_stack == []:
            answer[i] = -1

        # else add the last element of monotonic stack to its respective position in answer array
        else:
            answer[i] = monotonic_stack[-1]

        # add the traversed element to monotonic stack
        monotonic_stack.append(numbers[i])

    return answer  # return the answer array


if __name__ == "__main__":
    arr = [4, 12, 5, 31, 2, 5]
    arr1 = [12, 3, 5, 8, 1, 67]
    print(next_greater(arr))  # [12, 31, 31, -1, 5, -1]
    print(next_greater(arr1))  # [67, 5, 8, 67, 67, -1]
   
