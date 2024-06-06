from scipy import sparse
a = sparse.dok_matrix((10, 5))
a[2, 3] = 1.0
a[3, 3] = 2.0
a[4, 3] = 3.0

print(a.keys())
print(a.values())

# dict_keys([(2, 3), (3, 3), (4, 3)])
# dict_values([1.0, 2.0, 3.0])

w = sparse.dok_matrix((4, 4))

edges = [(0, 1, 10), (1, 2, 5), (0, 2, 3),
        (2, 3, 7), (3, 0, 4), (3, 2, 6)]

for i, j, v in edges:
    w[i, j] = v

w.todense()

print(w)

# dict_keys([(2, 3), (3, 3), (4, 3)])
# dict_values([1.0, 2.0, 3.0])
#   (0, 1)        10.0
#   (1, 2)        5.0
#   (0, 2)        3.0
#   (2, 3)        7.0
#   (3, 0)        4.0
#   (3, 2)        6.0
