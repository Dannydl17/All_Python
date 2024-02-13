test_list = [
    [0, 0, 0],
    [0, 0, 0],
]
for i, val in enumerate(test_list):
    for j, _ in enumerate(val):
        test_list[i][j] = 5

print(test_list)
