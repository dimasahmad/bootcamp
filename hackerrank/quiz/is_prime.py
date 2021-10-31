def is_prime(n: int) -> bool:
    if n > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(n / 2) + 1):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (n % i) == 0:
                return False
        else:
            return True

    else:
        return False