#Write a short Python function, is even(k), that takes an integer value and returns True if k is even, and False otherwise. However, your function cannot use the multiplication, modulo, or division operators. 

def main(n):
    if n & 1 == 0:
        return True
    else:        return False

if __name__ == "__main__":
    print(main(10))
    print(main(3))
    print(main(-2))
    print(main(0))
    print(main(-3))
