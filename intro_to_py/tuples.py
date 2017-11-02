dimensions = 15, 14, 100, 33, 459, 10, 60
# print(dimensions)
a, b, c, d, e, f, g = dimensions
# print(a, b, c, d, e, f, g)
# print('The dimensions are: {} : {} : {} : {} : {} : {} : {}'.format(a, b, c, d, e, f, g))

# Can use tuples as keys for a dict

def first_and_last(sequence):
    return sequence[0], sequence[-1]

print(first_and_last((a, b, c, d, e, f, g)))
