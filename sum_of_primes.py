
def is_prime(i):
    if i < 2: return False
    if i == 2: return True
    for cnt in range(2, i):
        if i % cnt == 0:
            return False
    return True

if __name__ == "__main__":
    i = 0
    cnt = 0
    primes = []
    while True:
        i += 1
        if is_prime(i):
            primes.append(i)
            cnt += 1
        if cnt == 1000: break
    print sum(primes)


