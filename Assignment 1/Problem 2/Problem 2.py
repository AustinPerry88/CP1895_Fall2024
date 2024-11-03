class Person:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Customer(Person):
    def __init__(self, first_name, last_name, email, customer_number):
        super().__init__(first_name, last_name, email)
        self.customer_number = customer_number

class Employee(Person):
    def __init__(self, first_name, last_name, email, ssn):
        super().__init__(first_name, last_name, email)
        self.ssn = ssn

def create_customer():
    print("\nDATA ENTRY")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email = input("Email: ")
    customer_number = input("Number:  ")
    return Customer(first_name, last_name, email, customer_number)

def create_employee():
    print("\nDATA ENTRY")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email = input("Email: ")
    ssn = input("SSN: ")
    return Employee(first_name, last_name, email, ssn)

def display_person_type(person):
    if isinstance(person, Customer):
        print("\nCUSTOMER")
        print("Name:\t\t{}".format(person.get_full_name()))
        print("Email:\t\t{}".format(person.email))
        print("Number:\t\t{}".format(person.customer_number))
    if isinstance(person, Employee):
        print("\nEMPLOYEE")
        print("Name:\t\t{}".format(person.get_full_name()))
        print("Email:\t\t{}".format(person.email))
        print("SSN:\t\t{}".format(person.ssn))


# Main program
def main():
    print('Customer/Employee Data Entry')
    while True:
        type = input("\nCustomer or employee? (c/e): ").lower()
        if type == 'c':
            person = create_customer()

        elif type == 'e':
            person = create_employee()

        else:
            print("Invalid option. Please enter 'c' for customer or 'e' for employee.")
            continue

        display_person_type(person)

        choice = input("\nContinue? (y/n): ").lower()
        if choice == 'n':
            print("\nBye!")
            break

if __name__ == "__main__":
    main()
