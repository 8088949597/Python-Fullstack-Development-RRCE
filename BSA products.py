# ------------------ Data Storage ------------------
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "seller1": {"password": "seller123", "role": "seller"},
    "buyer1": {"password": "buyer123", "role": "buyer"}
}

products = {}  # product_id : {name, price, qty}
orders = []

# ------------------ Logadmin
# in ------------------
def login():
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]["password"] == password:
        print(f"\nLogin successful as {users[username]['role']}\n")
        return users[username]["role"]
    else:
        print("Invalid credentials\n")
        return None

# ------------------ Admin Functions ------------------
def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. View Users")
        print("2. Delete User")
        print("3. Logout")

        choice = input("Choose: ")

        if choice == "1":
            print("\nUsers:")
            for u, d in users.items():
                print(u, "-", d["role"])

        elif choice == "2":
            user = input("Enter username to delete: ")
            if user in users and users[user]["role"] != "admin":
                del users[user]
                print("User deleted successfully")
            else:
                print("Cannot delete admin or user not found")

        elif choice == "3":
            break

# ------------------ Seller Functions ------------------
def seller_menu():
    while True:
        print("\n--- Seller Menu ---")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. Logout")

        choice = input("Choose: ")

        if choice == "1":
            pid = input("Product ID: ")
            name = input("Product Name: ")
            price = float(input("Price: "))
            qty = int(input("Quantity: "))
            products[pid] = {"name": name, "price": price, "qty": qty}
            print("Product added")

        elif choice == "2":
            pid = input("Product ID to update: ")
            if pid in products:
                products[pid]["price"] = float(input("New Price: "))
                products[pid]["qty"] = int(input("New Quantity: "))
                print("Product updated")
            else:
                print("Product not found")

        elif choice == "3":
            pid = input("Product ID to delete: ")
            if pid in products:
                del products[pid]
                print("Product deleted")
            else:
                print("Product not found")

        elif choice == "4":
            break

# ------------------ Buyer Functions ------------------
def buyer_menu():
    while True:
        print("\n--- Buyer Menu ---")
        print("1. View Products")
        print("2. Search Product")
        print("3. Order Product")
        print("4. Logout")

        choice = input("Choose: ")

        if choice == "1":
            print("\nAvailable Products:")
            for pid, p in products.items():
                print(pid, p["name"], p["price"], p["qty"])

        elif choice == "2":
            search = input("Enter product name: ")
            for p in products.values():
                if search.lower() in p["name"].lower():
                    print(p)

        elif choice == "3":
            pid = input("Enter product ID: ")
            qty = int(input("Quantity: "))
            if pid in products and products[pid]["qty"] >= qty:
                products[pid]["qty"] -= qty
                orders.append(pid)
                print("Order placed successfully")
            else:
                print("Product unavailable or insufficient quantity")

        elif choice == "4":
            break

# ------------------ Main Program ------------------
while True:
    print("\n=== Online Shopping System ===")
    role = login()

    if role == "admin":
        admin_menu()
    elif role == "seller":
        seller_menu()
    elif role == "buyer":
        buyer_menu()