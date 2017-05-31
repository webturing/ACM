CARDS = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}


def foo(cards):
    tot = sum(CARDS[card.strip()] for card in cards)
    if tot > 21:
        return 0
    if tot <= 11 and 'A' in cards:
        tot += 10
    return tot


while True:
    n, m = map(int, raw_input().strip().split())
    host, guest = raw_input().strip().split(), raw_input().strip().split()
    host, guest = foo(host), foo(guest)
    if host >= guest:
        print '%d vs %d HOST WIN' % (host, guest)
    else:
        print '%d vs %d GUEST WIN' % (host, guest)
