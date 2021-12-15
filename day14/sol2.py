import sys
from functools import lru_cache
input = '\n'.join([x.strip() for x in sys.stdin.readlines()])

template, pair_insertion = input.split('\n\n')

rules = {}
for line in pair_insertion.split('\n'):
    pair, out = line.split(' -> ')
    rules[pair] = out

@lru_cache(maxsize=None)
def generate_frequencies(poly: str, step: int) -> dict:
    count = {}
    if step == 0:
        for p in poly:
            if p not in count:
                count[p] = 0
            count[p] += 1
        return count
    elif len(poly) == 2:
        
        count1 = generate_frequencies(poly[0] + rules[poly] + poly[1], step-1)
        for key in count1:
            if key not in count:
                count[key] = 0
            count[key] += count1[key]

        return count
    else:
        i = 0
        while i < len(poly)-1:
            new_count = generate_frequencies(poly[i] + poly[i+1], step)
            for key in new_count:
                if key not in count:
                    count[key] = 0
                count[key] += new_count[key]
            count[poly[i+1]] -= 1
            i += 1
        if poly[-1] not in count:
            count[poly[-1]] = 0
        count[poly[-1]] += 1
        return count

freqs = generate_frequencies(template, 40)
print(max(freqs.values()) - min(freqs.values()))
