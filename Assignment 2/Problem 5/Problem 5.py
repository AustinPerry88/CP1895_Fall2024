def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def main():
    print("Greatest Common Divisor")
    while True:
        num1 = int(input("\nNumber 1: "))
        num2 = int(input("Number 2: "))

        # Ensure that num1 is greater than num2
        if num1 < num2:
            print("Number 1 must be greater than Number 2. Please try again.")
            continue

        result = gcd(num1, num2)
        print(f"Greatest common divisor: {result}")

        # Ask user if they want to continue
        cont = input("\nContinue? (y/n): ").lower()
        if cont != 'y':
            print("\nBye!")
            break

if __name__ == "__main__":
    main()
