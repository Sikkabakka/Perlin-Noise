
size = 5

ting = [[i+j for i in range(size +1)] for j in range(size +1)]

for i in range(size):
    for j in range(size):
        print(ting[i][j])