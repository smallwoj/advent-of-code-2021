import sys
from typing import Counter
input = '\n'.join([x.strip() for x in sys.stdin.readlines()])

template, pair_insertion = input.split('\n\n')

rules = {}
for line in pair_insertion.split('\n'):
    pair, out = line.split(' -> ')
    rules[pair] = out

poly = template.strip()

cache = {}
for step in range(10):
    print(f'Step {step}')
    # print('cache:', cache)
    cache_hits = []
    new_poly = ''
    poly_copy = poly.strip()
    for key in cache:
        while key in poly_copy:
            cache_hits.append((key, poly.index(key)))
            poly_copy = poly_copy.replace(key, '_'*len(key), 1)

    i = 0
    while i < len(poly)-1:
        if i in map(lambda x: x[1], cache_hits):
            cached = filter(lambda x: x[1] == i, cache_hits)
            new_poly += cache[cached[1]]
            i += len(cached[1])
        else:
            
            new_poly += poly[i]
            new_poly += rules[poly[i] + poly[i+1]]
            i += 1
    new_poly += poly[-1]
    cache[poly] = new_poly
    poly = new_poly

freqs = Counter(poly)
print(max(freqs.values()) - min(freqs.values()))
# print(poly)
