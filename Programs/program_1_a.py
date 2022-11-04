# Program to find simple interest


def simple_interest(p: float, r: float, t: float) -> float:
    return p * r * t / 100


# Program to find compound interest


def compound_interest(p: float, r: float, t: float) -> float:
    return p * (1 + r / 100) ** t - p


if __name__ == "__main__":
    p = float(input("Enter principal amount: "))
    r = float(input("Enter rate of interest: "))
    t = float(input("Enter time period: "))
    print("Simple interest is", simple_interest(p, r, t))
    print("Compound interest is", compound_interest(p, r, t))
