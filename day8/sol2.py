import sys
input = [x.strip() for x in sys.stdin.readlines()]

sum = 0
for line in input:
    signal, output = line.split(' | ')
    display = {
        'top': set(),
        'middle': set(),
        'bottom': set(),
        'topleft': set(),
        'topright': set(),
        'bottomleft': set(),
        'bottomright': set(),
    }
    mapping = {}
    signals = signal.split()
    # find the signals with unique characters
    one = list(filter(lambda x: len(x) == 2, signals))[0]
    seven = list(filter(lambda x: len(x) == 3, signals))[0]
    four = list(filter(lambda x: len(x) == 4, signals))[0]
    eight = list(filter(lambda x: len(x) == 7, signals))[0]
    found = set()
    # start with eight, everything is possible
    for d in display:
        display[d].update(set(eight))

    # make some connections, 1 only has 2 parts
    display['topright'] = display['topright'].intersection(set(one))
    display['bottomright'] = display['bottomright'].intersection(set(one))
    # we can remove the sides from the listings
    display['top'] = display['top'].difference(display['topright'])
    display['bottom'] = display['bottom'].difference(display['topright'])
    display['middle'] = display['middle'].difference(display['topright'])
    display['bottomleft'] = display['bottomleft'].difference(display['topright'])
    display['topleft'] = display['topleft'].difference(display['topright'])

    # 7 only has 3 parts, top has to be the one that isnt on the sides
    display['top'] = display['top'].intersection(set(seven) - display['topright'])
    found.update(display['top'])
    # we can remove the top from the listing
    display['middle'] = display['middle'].difference(display['top'])
    display['bottom'] = display['bottom'].difference(display['top'])
    display['bottomleft'] = display['bottomleft'].difference(display['top'])
    display['topleft'] = display['topleft'].difference(display['top'])

    # 4 has 4 parts, top left and middle has to be the ones that arent on the sides
    display['topleft'] = display['topleft'].intersection(set(four) - display['topright'])
    display['middle'] = display['middle'].intersection(set(four) - display['topright'])
    # we can remove these potentials from the listings
    display['bottom'] = display['bottom'].difference(display['topleft'])
    display['bottomleft'] = display['bottomleft'].difference(display['topleft'])

    # update the mappings with the known values
    mapping[one] = '1'
    mapping[seven] = '7'
    mapping[four] = '4'
    mapping[eight] = '8'

    # isolate 6.
    for s in signals:
        if len(s) == 6:
            if len(display['bottomright'].intersection(set(s))) == 1:
                display['bottomright'] = display['bottomright'].intersection(set(s))
                found.update(display['bottomright'])
                display['topright'] = display['topright'].difference(display['bottomright'])
                found.update(display['topright'])
                mapping[s] = '6'
                break


    # isolate 0.
    for s in signals:
        if len(s) == 6:
            if len(display['topleft'].intersection(set(s))) == 1:
                display['topleft'] = display['topleft'].intersection(set(s))
                found.update(display['topleft'])
                display['middle'] = display['middle'].difference(display['topleft'])
                found.update(display['middle'])
                mapping[s] = '0'
                break


    # at this point its only bottomleft and bottom
    # isolate 3.
    for s in signals:
        if len(s) == 5:
            if len(display['bottom'].intersection(set(s))) == 1 and len(display['topleft'].intersection(set(s))) == 0:
                display['bottom'] = display['bottom'].intersection(set(s))
                found.update(display['bottom'])
                display['bottomleft'] = display['bottomleft'].difference(display['bottom'])
                found.update(display['bottomleft'])
                mapping[s] = '3'
                break


    # display should be complete, complete the mapping
    for s in signals:
        set_s = set(s)
        if len(s) == 5:
            # check 2
            if display['top'].intersection(set_s) and \
               display['topright'].intersection(set_s) and \
               display['middle'].intersection(set_s) and \
               display['bottomleft'].intersection(set_s) and \
               display['bottom'].intersection(set_s):
                mapping[s] = '2'
            # check 3
            elif display['top'].intersection(set_s) and \
               display['topleft'].intersection(set_s) and \
               display['middle'].intersection(set_s) and \
               display['bottomright'].intersection(set_s) and \
               display['bottom'].intersection(set_s):
                mapping[s] = '5'
    
    # finally, 9
    for s in signals:
        if len(s) == 6 and s not in mapping:
            mapping[s] = '9'
    
    mapped = []
    for out in output.split():
        for mapp in mapping:
            if set(out) == set(mapp):
                mapped.append(mapping[mapp])
                break
    sum += int(''.join(mapped))

print(sum)
