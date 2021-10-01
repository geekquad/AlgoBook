# defining lowest_common_multiple function
def lowest_common_multiple(list1):
    if list1[0] == list1[1]:
        return list1[0]
    else:
        min_num = min(list1)
        max_num = max(list1)
        counter = 1
        while(True):
            if min_num*counter % max_num == 0:
                return min_num*counter
            counter += 1


# accepting two numbers from user in a list
list1 = list(map(int, input().split()))
# printing the lowest common multiple
print(f"Lowest Common Multiple is : {lowest_common_multiple(list1)}")
