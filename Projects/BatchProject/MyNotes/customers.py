customers = {}

def register_customer():
    customer_id = input("Enter Customer ID: ")
    name = input("Enter Customer Name: ")
    customers[customer_id] = {"name": name}
    print("Customer registered successfully!")

def display_customers():
    if not customers:
        print("No customers registered.")
        return
    print("\n--- Customer List ---")
    for cid, details in customers.items():
        print(f"ID: {cid}, Name: {details['name']}")

def customer_menu():
    while True:
        print("\n--- Customer Management ---")
        print("1. Register Customer")
        print("2. Display Customers")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            register_customer()
        elif choice == "2":
            display_customers()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
