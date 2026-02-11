import sys

#!/usr/bin/env python3

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main(argv):
    if len(argv) > 1:
        s = argv[1]
    else:
        s = input("Enter a non-negative integer: ").strip()
    try:
        n = int(s)
    except ValueError:
        print("Invalid integer:", s, file=sys.stderr)
        return 1
    if n < 0:
        print("Number must be non-negative", file=sys.stderr)
        return 1
    print(factorial(n))
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))