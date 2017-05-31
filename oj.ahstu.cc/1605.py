s = raw_input().strip()
dp = {}


def f(s):
    if s in dp.keys():
        print dp[s]
    if s == s[::-1]:
        dp[s] = 0
        return dp[s]
    mn = 0xffff
    for i in xrange(len(s) - 1):
        t = s[0:i] + s[i + 1] + s[i] + s[i + 2:]
        mn = min(mn, f(t) + 1)
    dp[s] = mn
    return mn


print f(s)