

def c(n, k):
    if k == n or k == 0:
        return 1
    if k != 1:
        return c(n - 1, k) + c(n - 1, k - 1)
    else:
        return n


n, k = map(int, input().split())
print(c(n, k))