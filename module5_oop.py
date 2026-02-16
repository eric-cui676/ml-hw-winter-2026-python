class NumberCollection:
    def __init__(self):
        self.numbers = []

    def insert(self, number):
        self.numbers.append(number)

    def search(self, x):
        for i in range(len(self.numbers)):
            if self.numbers[i] == x:
                return i + 1
        return -1


def main():
    collection = NumberCollection()

    n = int(input("Enter N (positive integer): "))

    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        collection.insert(num)

    x = int(input("Enter X to search for: "))
    result = collection.search(x)
    print(result)


if __name__ == "__main__":
    main()
