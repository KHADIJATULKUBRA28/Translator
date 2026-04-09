def prime(n):
    """Returns the nth prime number."""
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num