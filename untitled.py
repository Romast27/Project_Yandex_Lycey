st = ''
for i in range(1, 97):
    k = 0
    for j in range(2, i):
        if i % j == 0:
            k = 1
    if not k:
        st += str(i) + ', '
st += '97'