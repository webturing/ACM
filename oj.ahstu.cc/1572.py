for case in xrange(int(raw_input())):
    pipes, size = [], int(raw_input())
    for i in xrange(size):
        pipes.append(map(int, raw_input().strip().split()))
    pipes = sorted(pipes, key=lambda t: (-t[0], t[1], -t[2]))
    print pipes[0][2]