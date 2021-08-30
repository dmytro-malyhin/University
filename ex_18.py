a = [54, 32, 64, 762, 32, 544]
while len(a) > 0:
    last = a.pop()
    if last % 2 != 0:
        print('No')
        break
else:
    print('Yes')
