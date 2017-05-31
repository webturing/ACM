def check(exp):
    stack = []
    for char in exp:
        if char in '([':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return False
            else:
                stack.pop(-1)
        else:
            if len(stack) == 0 or stack[-1] != '[':
                return False
            else:
                stack.pop(-1)
    return len(stack) == 0


for case in xrange(int(raw_input())):
    print 'Yes' if check(raw_input()) else 'No'
