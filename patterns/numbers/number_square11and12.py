def pattern11(size):
    for i in range(1, size + 1):
        count = size * i
        for j in range(1, size + 1):
            if count < 10:
                print(0, end='')

            print(count, end=' ')
            count -= 1
        print()


def pattern12(size):
    for i in range(size, 0, -1):
        count = size * i
        for j in range(1, size + 1):
            if count < 10:
                print(0, end='')

            print(count, end=' ')
            count -= 1
        print()


def main():
    size = int(input())
    pattern11(size)
    print(end='\n\n')
    pattern12(size)


if __name__ == '__main__':
    main()
