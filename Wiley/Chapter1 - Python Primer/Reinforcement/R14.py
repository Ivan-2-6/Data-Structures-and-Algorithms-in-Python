# Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive integers smaller than n.

# --- Option 1: The Clean Loop ---
# Time Complexity: O(N)
# Space Complexity: O(1)
def sum_of_squares_iterative(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

# --- Option 2: The Pythonic Generator ---
# Time Complexity: O(N)
# Space Complexity: O(1)
def sum_of_squares_pythonic(n):
    return sum(i * i for i in range(n))

# --- Option 3: The Math Formula (Elite) ---
# Time Complexity: O(1) -> Instant, regardless of how big 'n' is.
# Space Complexity: O(1)
def sum_of_squares_math(n):
    return (n - 1) * n * (2 * n - 1) // 6


if __name__ == "__main__":
    # 1. Correctness Test (Are they all giving the same answer?)
    n_small = 5
    print("--- CORRECTNESS TEST (n = 5) ---")
    print(f"Iterative Output: {sum_of_squares_iterative(n_small)}")
    print(f"Pythonic Output:  {sum_of_squares_pythonic(n_small)}")
    print(f"Math O(1) Output: {sum_of_squares_math(n_small)}")
