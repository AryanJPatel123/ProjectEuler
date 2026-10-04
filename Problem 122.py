def search(chain, d, k):
    last = chain[-1]
    if last == k:
        return True
    remaining = d - (len(chain) - 1)
    if remaining == 0 or last * (2**remaining) < k:   # can't reach k even with largest currently possible jump
        return False
    for x in reversed(chain):                      # try largest jumps first
        nxt = last + x
        if nxt <= k:                            # if the largest jump falls short of (or hits) the target
            chain.append(nxt)                   # add the most recently calculated value to the chain
            if search(chain, d, k):             # recurse the search with new value added
                return True                     # means value has been found
            chain.pop()                         # if the target cant be found then discard the last added value
    return False

def shortest_chain(k):
    d = (k - 1).bit_length()                       # ceiling(log2 k), the lower bound
    while True:
        chain = [1]                                 # initialise the chain
        if search(chain, d, k):
            return chain                           # len(chain) - 1 multiplications
        d = d + 1
list1 = []
for k in range(1, 201):
    c = shortest_chain(k)
    list1.append(len(c) - 1)

print(sum(list1))