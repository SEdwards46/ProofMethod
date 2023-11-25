# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False #Base Case; numbers less than or equal to one not prime
    if n <= 3:
        return True #Base Case; 2 and 3 are prime
    if n % 2 == 0 or n % 3 == 0:
        return False #Check for divisibilty by 2 or 3
    i = 5 # Start checking for primality from 5 and use a 6k ± 1 optimization
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: 
            return False  # If n is divisible by i or i + 2, it's not prime
        i += 6
    return True  # If no factors were found, the number is prime

# Function to find and verify perfect numbers for prime values of 'n' up to a specified limit
def find_perfect_numbers(limit):
    for n in range(2, limit):
        if is_prime(n):
            mersenne_prime = 2**n - 1
            if is_prime(mersenne_prime):
              # Calculate the perfect number using the formula for even perfect numbers
                perfect_number = (2**(n - 1)) * mersenne_prime
                print(f"n = {n}, Perfect Number = {perfect_number}")
               # Calculate and print the divisors of the perfect number
                divisors = [i for i in range(1, perfect_number) if perfect_number % i == 0]
                print(f"Divisors of the Perfect Number: {divisors}\n")

# Call the function to find perfect numbers for prime values of 'n' up to 10
find_perfect_numbers(10)