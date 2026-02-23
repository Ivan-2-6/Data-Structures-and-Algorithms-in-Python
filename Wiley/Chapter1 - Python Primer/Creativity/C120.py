# Python’s random module includes a function shu#e(data) that accepts a
# list of elements and randomly reorders the elements so that each possi-
# ble order occurs with equal probability. The random module includes a
# more basic function randint(a, b) that returns a uniformly random integer
# from a to b (including both endpoints). Using only the randint function,
# implement your own version of the shu#e function.



import random

# Time Complexity: O(N) because we iterate through the list exactly once.
# Space Complexity: O(1) because we swap in-place and use no extra memory.
def my_shuffle(data):
    # Start from the last index and move backwards down to 1
    # range(start, stop, step)
    for i in range(len(data) - 1, 0, -1):
        
        # Pick a random integer from 0 up to 'i' (inclusive)
        # This is where randint(a, b) does the heavy lifting
        random_index = random.randint(0, i)
        
        # Swap the element at the current index 'i' with the randomly chosen index
        data[i], data[random_index] = data[random_index], data[i]

    # Note: We do not return anything because the list is modified in-place

# ==========================================
# TEST ARENA
# ==========================================
if __name__ == '__main__':
    # Initialize a sorted dataset
    dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print(f"Original: {dataset}")
    
    # Shuffle it using our custom algorithm
    my_shuffle(dataset)
    
    print(f"Shuffled: {dataset}")
