def gcd(a, b):
    if b:
        return gcd(b, a % b)
    else:
        return a


def lcm(a, b):
    return a * b / gcd(a, b)


a, b = map(int, raw_input().strip().split())
print lcm(a, b)