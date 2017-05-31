num, hegiht = map(int, raw_input().strip().split())
apples = map(int, raw_input().strip().split())
unreaches = [apple for apple in apples if hegiht + 30 < apple]
print len(unreaches)
