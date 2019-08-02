def fibonacci(N):
    cache = {0: 0, 1: 1}
    def helper(N):
        if N in cache:
            return cache[N]
        else:
            cache[N] = helper(N - 2) + helper(N - 1)
        return cache[N]
    return helper(N)

def test_fibonacci():
    assert fibonacci(6) == 8