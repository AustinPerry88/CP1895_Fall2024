import csv
from S3_customer_class import Customer


def read_customer_data(filename):
    customer_list = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        for row in reader:
            cust_id, first_name, last_name, company, address, city, state, zip_code = row
            customer = Customer(cust_id, first_name, last_name, company, address, city, state, zip_code)
            customer_list.append(customer)

    return customer_list


def main():
    customer_list = read_customer_data('customers.csv')
    print("Customer Viewer")
    while True:
        customer_id = input("\nEnter customer ID: ")

        found = False
        for customer in customer_list:
            if customer.id == customer_id:
                print()
                print(customer.get_full_address())
                found = True
                break

        if not found:
            print("\nNo customer with that ID.")

        continue_choice = input("\nContinue? (y/n): ")
        if continue_choice.lower() != 'y':
            print("\nBye!")
            break


if __name__ == "__main__":
    main()

