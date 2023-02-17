def solution(numer1, denom1, numer2, denom2):
    gcd = 1
    a = numer1 * denom2 + numer2 * denom1
    b = denom1 * denom2
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            gcd = i
            break
    answer = [a // gcd, b // gcd]
    return answer