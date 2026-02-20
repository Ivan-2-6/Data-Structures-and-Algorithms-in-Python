import time

# --- Option 1: Your Pythonic Generator ---
# Time Complexity: O(N)
# Space Complexity: O(1)
def odd_squares_sum_iterative(n):
    return sum(i * i for i in range(1, n, 2))


# --- Option 2: The Math Formula (Elite) ---
# Time Complexity: O(1) -> Instant
# Space Complexity: O(1)
def odd_squares_sum_math(n):
    k = n // 2  # Find exactly how many odd numbers exist below n
    return (k * (2 * k - 1) * (2 * k + 1)) // 3


if __name__ == "__main__":
    # 1. Correctness Test
    n_small = 6
    print("--- CORRECTNESS TEST (n = 6) ---")
    print(f"Iterative Output: {odd_squares_sum_iterative(n_small)}")
    print(f"Math O(1) Output: {odd_squares_sum_math(n_small)}")
    
    # 2. Performance Test
    n_large = 10_000_000
    print(f"\n--- PERFORMANCE TEST (n = 10,000,000) ---")
    
    start_time = time.time()
    odd_squares_sum_iterative(n_large)
    print(f"Iterative Time: {time.time() - start_time:.5f} seconds")
    
    start_time = time.time()
    odd_squares_sum_math(n_large)
    print(f"Math O(1) Time: {time.time() - start_time:.5f} seconds")
