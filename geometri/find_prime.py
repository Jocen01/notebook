n = 2
i = 1
while n * n <= k:
    if k % n == 0:
        k = k/n
        i += 1
    else:
        n += 2
