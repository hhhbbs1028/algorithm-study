t = int(input())
for _ in range(t):
    n = int(input())
    X = list(map(int, input().split()))

    orig = sum(abs(X[i] - X[i-1]) for i in range(1, n))

    best_gain = 0
    for k in range(1, n-1):
        gain = abs(X[k] - X[k-1]) + abs(X[k+1] - X[k]) - abs(X[k+1] - X[k-1])
        best_gain = max(best_gain, gain)

    print(orig - best_gain)
