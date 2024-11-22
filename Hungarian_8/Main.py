from Hungarian_8.HungarianAlg import HungarianAlg

cost_matrix = [
    [4, 2, 8],
    [2, 4, 6],
    [7, 5, 3]
]

hungarian = HungarianAlg(cost_matrix)
assignments = hungarian.solve()
print("Optimal assignments:", assignments)
