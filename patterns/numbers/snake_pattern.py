def pattern(size):
    for i in range(1, size + 1):
        if i % 2 == 0:
            print(i + 1, end=' ')

        for j in range(1, size):
            print(i, end=' ')

        if i % 2 == 1:
            print(i + 1, end=' ')

        print()


def main():
    size = int(input())
    pattern(size)


if __name__ == '__main__':
    main()
