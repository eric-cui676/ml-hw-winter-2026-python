from module5_mod import NumberCollection


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
