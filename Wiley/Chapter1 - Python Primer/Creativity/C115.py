# ==========================================
# C-1.15: Distinct Elements
# ==========================================

# --- Option 1: The Fixed Brute Force (Beginner) ---
# Time: O(N^2) | Space: O(1)
def distinct_brute(my_list):
    for num in my_list:
        # Notice we don't use 'else: return True' inside the loop.
        # We only return True after surviving the ENTIRE loop.
        if my_list.count(num) > 1:
            return False
    return True


# --- Option 2: The Sorting Approach (Interview Standard) ---
# Time: O(N log N) | Space: O(1)
# Use this if the interviewer says "Do not use extra memory / sets"
def distinct_sorted(my_list):
    # .sort() modifies the list in-place
    my_list.sort()
    # Loop up to the second-to-last item to avoid IndexError
    for i in range(len(my_list) - 1):
        if my_list[i] == my_list[i + 1]:
            return False
    return True


# --- Option 3: The Set Approach (Data Scientist / GATE DA Standard) ---
# Time: O(N) | Space: O(N)
# This is the fastest, cleanest, and most Pythonic way.
def distinct_set(my_list):
    # If the set (which destroys duplicates) is the same size as the list, 
    # it means there were no duplicates to destroy.
    return len(set(my_list)) == len(my_list)


if __name__ == '__main__':
    # Test Case 1: Has duplicates
    seq1 = [1, 3, 3, 3, 5]
    
    # Test Case 2: All distinct (This would have failed your original code)
    seq2 = [100, 200, 300, 400]
    
    print(f"Testing seq1 {seq1}:")
    print("Brute: ", distinct_brute(seq1))
    print("Sorted:", distinct_sorted(seq1.copy()))
    print("Set:   ", distinct_set(seq1))
    
    print(f"\nTesting seq2 {seq2}:")
    print("Brute: ", distinct_brute(seq2))
    print("Sorted:", distinct_sorted(seq2.copy()))
    print("Set:   ", distinct_set(seq2))
