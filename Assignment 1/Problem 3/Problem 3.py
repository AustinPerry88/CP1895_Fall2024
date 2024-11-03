from random import randint

class RandomIntList:
    def __init__(self, size):
        self.count = size
        self.int_list = []
        self.fill()

    def fill(self):
        for _ in range(self.count):
            self.int_list.append(randint(1, 100))

    def get_count(self):
        return self.count

    def get_total(self):
        return sum(self.int_list)

    def get_average(self):
        return self.get_total() / self.get_count()

    def __str__(self):
        return ", ".join(map(str, self.int_list))

def main():
    print("Random Integer List\n")
    n = int(input("How many random integers should the list contain?: "))
    while True:
        try:
            if n <= 0:
                raise ValueError("The number of integers must be a positive integer.")
            int_list = RandomIntList(n)
            print("\nRandom Integers")
            print("=" * 15)
            print(f"Integers: {int_list}")
            print(f"Count: {int_list.get_count()}")
            print(f"Total: {int_list.get_total()}")
            print(f"Average: {int_list.get_average()}")
        except ValueError as e:
            print(f"Error: {e}")
            continue


        choice = input("\nContinue? (y/n): ").strip().lower()
        if choice == 'n':
            print("\nBye!")
            break

if __name__ == "__main__":
    main()
