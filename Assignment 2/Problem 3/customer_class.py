class Customer:
    def __init__(self, id, first_name, last_name, company, address, city, state, zip):
        self.id = id
        self.firstName = first_name
        self.lastName = last_name
        self.company = company
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

    def get_full_address(self):
        if self.company:
            return f"{self.firstName} {self.lastName}\n{self.company}\n{self.address}\n{self.city}, {self.state} {self.zip}"
        else:
            return f"{self.firstName} {self.lastName}\n{self.address}\n{self.city}, {self.state} {self.zip}"
