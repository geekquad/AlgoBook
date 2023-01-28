"""
Next Greater Element

Given an array of integers . Our goal is to  return an answer array which contains 
Next greater element of every elements in an array. if an element don't have any greater 
element. we add -1. 

Examples:

numbers = [ 4, 12, 5, 31, 2, 5]
answer = [ 12, 31, 31, -1, 5, -1]

Explanation:

First elemnt in numbers array is 4  -  for 4 next greater element is 12 . the next index itself so in answer array 
                                       we add 12 in the  answer array.

Next element in numbers array is 12 -  for 12 , the next element 5 is not greater than 12 so we move the next index 
                                       5 is also not greater so we move, 31 is greater.so we are add 31 in the answer array.
                                       
Next element in numbers array is 5  -  for 5, 31 is next greater element. so add 31 to answer array
                      

Next element in numbers array is 31 -  for 31 , there is no greater element , so we add -1

Next element in numbers array is 2  -  for 2 , 5 is a greater element , so we add 5.

Next element in numbers array is 5  -  5 is the last element, so there is no possibility of next greater element so we add -1


"""


def next_greater(numbers):
    monotonic_stack = []
    answer = [0 for i in range(len(numbers))]

    for i in range(len(numbers)-1, -1, -1):
        while monotonic_stack and monotonic_stack[-1] < numbers[i]:
            monotonic_stack.pop()
        if monotonic_stack == []:
            answer[i] = -1
        else:
            answer[i] = monotonic_stack[-1]
        monotonic_stack.append(numbers[i])
    return answer


if __name__ == "__main__":
    arr = [4, 12, 5, 31, 2, 5]
    arr1 = [12,3,5,8,1,67]
    print(next_greater(arr))  #[12, 31, 31, -1, 5, -1]
    print(next_greater(arr))  #[67, 5, 8, 67, 67, -1]
