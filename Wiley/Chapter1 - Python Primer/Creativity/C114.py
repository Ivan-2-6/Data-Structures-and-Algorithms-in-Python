#Write a short Python function that takes a sequence of integer values and determines if there is a distinct pair of numbers in the sequence whose product is odd.

# --- Option 1: Your Cleaned Up Logic (Distinct Indices) ---
# Time: O(N) | Space: O(1)
def odd_product_fast(my_list):
    odd_count = 0
    for num in my_list:
        if num % 2 != 0:
            odd_count += 1
            if odd_count == 2:
                return True # We found two odds. Stop the loop.
    return False

# --- Option 2: The Set Logic (Distinct Values) ---
# Time: O(N) | Space: O(N)
def odd_product_set(my_list):
    odd_uniques = set(num for num in my_list if num % 2 != 0)
    return len(odd_uniques) >= 2

if __name__ == "__main__":
    # Test Case 1: Has distinct odd numbers (3 and 5)
    seq1 = [2, 3, 4, 5, 6]
    print(f"Seq1 Fast: {odd_product_fast(seq1)}") # True
    print(f"Seq1 Set:  {odd_product_set(seq1)}")  # True
    
    # Test Case 2: Has duplicates, but NOT distinct values (only 3s)
    seq2 = [2, 3, 4, 3, 6]
    # Fast approach sees two 3s and says True
    print(f"\nSeq2 Fast: {odd_product_fast(seq2)}") # True 
    # Set approach deletes the duplicate 3, sees only one odd number, says False
    print(f"Seq2 Set:  {odd_product_set(seq2)}")  # False
