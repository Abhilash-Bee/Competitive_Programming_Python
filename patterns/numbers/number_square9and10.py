def pattern9(size):
    count = 1
    for i in range(size):
        for j in range(size):
            if count < 10:
                print(0, end='')

            print(count, end=' ')
            count += 1
        print()


def pattern10(size):
    count = size * size
    for i in range(size):
        for j in range(size):
            if count < 10:
                print(0, end='')

            print(count, end=' ')
            count -= 1
        print()


def main():
    size = int(input())
    pattern9(size)
    print(end='\n\n')
    pattern10(size)


if __name__ == '__main__':
    main()
