class Fibonacci:
    def __init__(self, n):
        self.n = n

    def calculate(self):
        if self.n < 0:
            raise ValueError("n must be a non-negative integer")
        if self.n == 0:
            return 0
        elif self.n == 1:
            return 1
        a, b = 0, 1
        for _ in range(self.n - 1):
            a, b = b, a + b
        return b
