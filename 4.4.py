try:
    n = int(input())
    count = n - 1
    x = n - 1
    while x > 0:
        if (x * x) % n == 0:
            count -= 1
        x -= 1
    print(count)
except:
    print()