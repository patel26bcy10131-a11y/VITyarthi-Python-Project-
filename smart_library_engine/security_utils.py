
import random

def generate_member_card_id(prefix="LIB", seed_num=None):
    # This Generates a pseudo random 6 digit member card ID using the random module
    if seed_num is not None:
        random.seed(seed_num)

    random_digits = random.randint(100000, 999999)
    return f"{prefix}-{random_digits}"

#  to check if the key is prime
def check_if_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True