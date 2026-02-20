#Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of a tuple of length two. Do not use the built-in functions min or max in implementing your solution.

def minmax(my_List):
    
    min_value = my_List[0]
    max_value = my_List[0]
    
    for i in range(1,len(my_List)):  # for num in my_list[1:]:
        if my_List[i] > max_value:
            max_value = my_List[i]
        elif my_List[i] < min_value:
            min_value = my_List[i]
            
    this_tuple = (min_value, max_value)
    return this_tuple       


if __name__ == "__main__":
    my_List = [-3, 0, 1, -2, 4]
    print (minmax(my_List))
