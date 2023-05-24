def pattern(size):
    for i in range(size):
        for j in range(size):
            print(chr(65 + i), end=' ')
        print()


def main():
    size = int(input())
    pattern(size)


if __name__ == '__main__':
    main()
