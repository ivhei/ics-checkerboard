n = input("Enter N: ")

if len(n) != 1 or n < "1" or n > "9":
    print("Invalid input! Enter 1-9.")
    exit(1)

n = int(n)

for row in range(n):
    for col in range(n):
        if (row + col) % 2 == 0:
            print("*", end="")
        else:
            print(".", end="")
    print()
