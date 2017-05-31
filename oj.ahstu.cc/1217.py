def bin2dec(b):
    s = 0
    for char in b.strip():
        s = 2 * s + (char == '1')
    return s


def dec2bin(d):
    s = ''
    while d > 0:
        s = list('01')[d % 2] + s
        d /= 2
    return s


exp = raw_input()

if '+' in exp:
    nums = map(bin2dec, exp.strip().split('+'))
    print dec2bin(nums[0] + nums[1])
else:
    nums = map(bin2dec, exp.strip().split('-'))
    print dec2bin(nums[0] - nums[1])
