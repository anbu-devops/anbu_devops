def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example usage:
ntime=int(input("How many times you want to check the prime number"))
for i in range(ntime+1):
    number = int(input("Enter a number: "))
    if is_prime(number):
        print(number, "is a prime number")
    else:
        print(number, "is not a prime number")