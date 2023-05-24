def pattern2(size):
    for i in range(size):
        for k in range(i):
            print('  ', end='')

        for j in range(i, (size - 1) * 2 - i + 1):
            if j <= size - 1:
                print((size - 1) - j, end=' ')
            else:
                print(j - (size - 1), end=' ')

        print()


def main():
    size = int(input())
    pattern2(size)


if __name__ == '__main__':
    main()
