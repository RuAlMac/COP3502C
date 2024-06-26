# Lab 10

def gradient(n, file=None):
    for i in range(n):
        for j in range(n):
            print((i + j) // 2, end=' ', file=file)
        print(file=file)


def square(n, file=None):
    for i in range(n):
        for j in range(n):
            print(min(i, j, n - i - 1, n - j - 1) * 2, end=" ", file=file)
        print(file=file)


def circle(n, file=None):
    for i in range(n):
        for j in range(n):
            distance = ((i - n/2) ** 2 + (j-n/2) ** 2) ** 0.5
            print(max(int(distance - n ** 0.5), 0),
                  end=" ", file=file)
        print(file=file)


def make_image(pattern, size, filename):
        with open(filename, "w") as file:
            file.write(f"P2 {size} {size} {size}\n")
            pattern(size, file)

make_image(square, 5, "square.pgm")