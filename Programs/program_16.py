# Program class to implement pow(x, n) function


class Power:
    def __init__(self, x: int, n: float):
        self.x = x
        self.n = n

    def __pow__(self):
        return self.x**self.n

    def __str__(self):
        return f"{self.x}^{self.n} = {self.__pow__()}"


if __name__ == "__main__":
    x = int(input("Enter x: "))
    n = float(input("Enter n: "))
    power = Power(x, n)
    print(power)
