def pattern(size):
    count = 0
    for i in range(size):
        for j in range(i + 1):
            print(chr(65 + count), end=' ')
            count += 1
        print()


def main():
    size = int(input())
    pattern(size)


if __name__ == '__main__':
    main()
