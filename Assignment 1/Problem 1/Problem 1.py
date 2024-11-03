class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_perimeter(self):
        # Calculate perimeter of the rectangle
        return 2 * (self.width + self.height)

    def get_area(self):
        # Calculate area of the rectangle
        return self.height * self.width

    def __str__(self):
        # String representation of the rectangle
        result = '* ' * self.width + '\n'  # Top border

        # Sides of the rectangle with gap in between
        for _ in range(self.height - 2):
            result += '*' + ' ' * (self.width * 2 - 3) + '*\n'

        result += '* ' * self.width  # Bottom border
        return result


class Square(Rectangle):
    def __init__(self, side):
        # Square is a special case of a rectangle, so initialize using the side
        super().__init__(side, side)


# Main program
def main():
    print('Rectangle Calculator\n')
    while True:
        choice = input('Rectangle or square? (r/s): ').lower()
        if choice == 'r':
            height = int(input('Height:\t\t'))
            width = int(input('Width:\t\t'))
            r = Rectangle(height, width)

            # Displaying information about the rectangle
            print('Perimeter:\t{}'.format(r.get_perimeter()))
            print('Area:\t\t{}'.format(r.get_area()))
            print(r)

        elif choice == 's':
            side = int(input('Length:\t\t'))
            s = Square(side)

            # Displaying information about the square
            print('Perimeter:\t{}'.format(s.get_perimeter()))
            print('Area:\t\t{}'.format(s.get_area()))
            print(s)
        else:
            print('Error: Invalid choice')

        repeat = input('\nContinue? (y/n): ')
        print()
        if repeat == 'n':
            print('\nBye!')
            break
    


if __name__ == "__main__":
    main()
