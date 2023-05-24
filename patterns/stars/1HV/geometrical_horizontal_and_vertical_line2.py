def horizontal_line(size):
    print('*' * size)


def vertical_line(size):
    for i in range(size):
        print('*')


def main():
    size = int(input())
    horizontal_line(size)
    print(end='\n\n')
    vertical_line(size)


if __name__ == '__main__':
    main()
