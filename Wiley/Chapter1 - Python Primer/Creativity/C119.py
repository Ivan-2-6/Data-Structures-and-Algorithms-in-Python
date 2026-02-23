# Demonstrate how to use Python’s list comprehension syntax to produce the list [ a , b , c , ..., z ], but without having to type all 26 such characters literally.

# ord('a') is 97. ord('z') + 1 is 123 (since range stop is exclusive).
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]

print(alphabet)
# Output: ['a', 'b', 'c', ..., 'z']
