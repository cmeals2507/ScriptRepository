# adapted from https://github.com/neilernst/cliffsDelta
def cliffs_delta(l1, l2):
    m, n = len(l1), len(l2)
    l2 = sorted(l2)
    j = more = less = 0
    
    for repeats, x in gen(sorted(l1)):
        while j <= (n - 1) and l2[j] < x:
            j += 1
        more += j * repeats
        while j <= (n - 1) and l2[j] == x:
            j += 1
        less += (n - j) * repeats
    d = (more - less) / (m * n)
    
    # Hess and Kromrey, 2004
    thresholds = {
        'small': 0.147,
        'medium': 0.33,
        'large': 0.474
    }
    size = 'negligible' if abs(d) < thresholds['small'] else 'small' if abs(d) < thresholds['medium'] else 'medium' if abs(d) < thresholds['large'] else 'large'
    
    return d, size

def gen(lst):
    '''Iterator, chunks repeated values.'''
    for j, two in enumerate(lst):
        if j == 0:
            one, i = two, 0
        if one != two:
            yield j - i, one
            i = j
        one = two
    yield j - i + 1, two