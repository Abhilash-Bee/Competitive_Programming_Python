def pattern(size):
    for i in range(1, size + 1):
        for j in range(size - i):
            print(' ', end='')

        count = 1
        for j in range(1, i + 1):
            print(count, end=' ')
            count = count * (i - j) // j
        print()


def main():
    size = int(input())
    pattern(size)


if __name__ == '__main__':
    main()
