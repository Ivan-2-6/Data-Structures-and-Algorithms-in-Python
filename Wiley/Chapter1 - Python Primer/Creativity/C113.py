#C-1.13 Write a pseudo-code description of a function that reverses a list of n integers, so that the numbers are listed in the opposite order than they were before, and compare this method to an equivalent Python function for doing the same thing.

# --- Option 1: Your Two-Pointer Algorithm ---
# Time: O(N) | Space: O(1)
def reverse_two_pointer(my_list):
    i = 0
    j = len(my_list) - 1
    while i < j:
        my_list[i], my_list[j] = my_list[j], my_list[i]
        i += 1
        j -= 1
    return my_list


# --- Option 2: Python Built-in (Fastest In-Place) ---
# Time: O(N) | Space: O(1)
def reverse_builtin(my_list):
    # .reverse() modifies the list and returns None, 
    # so we must execute it, then return the list.
    my_list.reverse() 
    return my_list


# --- Option 3: Python Slicing (Creates a Copy) ---
# Time: O(N) | Space: O(N) -> Uses extra memory!
def reverse_slicing(my_list):
    return my_list[::-1]


if __name__ == "__main__":
    # Test Data
    seq1 = [23, 34, 5, 1, 2, -4]
    seq2 = [23, 34, 5, 1, 2, -4]
    seq3 = [23, 34, 5, 1, 2, -4]
    
    print("1. Two-Pointer:", reverse_two_pointer(seq1))
    print("2. Built-in:   ", reverse_builtin(seq2))
    print("3. Slicing:    ", reverse_slicing(seq3))
