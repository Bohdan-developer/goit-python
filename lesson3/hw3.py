def main():
    n = int(input("Enter the range of numbers: "))

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 2) + fibonacci(n - 1)

    result = []
    start = 0
    for n in range(start, n+1):
        result.append(fibonacci(n))
    print(result)


if __name__ == "__main__":
    main()
