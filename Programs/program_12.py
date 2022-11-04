# Fabonicci series


def fabonicci(n: int) -> int:
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fabonicci(n - 1) + fabonicci(n - 2)


if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    for i in range(1, n + 1):
        print(fabonicci(i), end=" ")
