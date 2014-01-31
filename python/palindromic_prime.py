
def is_prime(i):
    if i < 2: return False
    if i == 2: return True
    for cnt in range(2, i):
        if i % cnt == 0:
            return False
    return True

def is_palindromic(i):
    str_i = str(i)
    if len(str_i) < 2: return True
    if str_i == str_i[::-1]:
        return True
    return False

if __name__ == "__main__":
    pps = []
    for i in range(1, 1001):
        if is_prime(i) and is_palindromic(i):
            pps.append(i)
    print max(pps)


