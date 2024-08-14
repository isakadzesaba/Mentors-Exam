def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def gap(g, m, n):
    previous_prime = None
    for i in range(m, n + 1):
        if is_prime(i):
            if previous_prime is not None and i - previous_prime == g:
                return [previous_prime, i]
            previous_prime = i
    return None
    


print(gap(2,100,103))