def pyramid_pattern(rows):
    print("\n🔺 Number Pyramid Pattern\n")

    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def reverse_pattern(rows):
    print("\n🔻 Reverse Number Pattern\n")

    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def floyd_triangle(rows):
    print("\n🔢 Floyd's Triangle\n")

    num = 1

    for i in range(1, rows + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()


def main():
    while True:
        print("\n==============================")
        print("🧠 NUMBER PATTERN GENERATOR")
        print("==============================")

        print("\n1. Pyramid Pattern")
        print("2. Reverse Pattern")
        print("3. Floyd's Triangle")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "4":
            print("\n👋 Exiting Program...")
            break

        try:
            rows = int(input("Enter number of rows: "))

            if rows <= 0:
                print("❌ Please enter positive number.")
                continue

            if choice == "1":
                pyramid_pattern(rows)

            elif choice == "2":
                reverse_pattern(rows)

            elif choice == "3":
                floyd_triangle(rows)

            else:
                print("❌ Invalid choice!")

        except ValueError:
            print("❌ Please enter valid number.")


main()