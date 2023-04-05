import pickle

def display_menu():
    print("Vegetable\tPrice")
    print("=========\t=====")

def display_vegetables(vegetables):
    for vegetable, price in vegetables.items():
        print(f"{vegetable}\t\t${price:.2f}")

def add_vegetable(vegetables):
    vegetable = input("Enter vegetable name: ")
    price = float(input("Enter vegetable price: "))
    vegetables[vegetable] = price
    print(f"{vegetable} has been added to the list of vegetables")

def change_vegetable_price(vegetables):
    vegetable = input("Enter vegetable name: ")
    if vegetable in vegetables:
        new_price = float(input("Enter new price: "))
        vegetables[vegetable] = new_price
        print(f"{vegetable}'s price has been updated to ${new_price:.2f}")
    else:
        print(f"{vegetable} is not in the list of vegetables")

def delete_vegetable(vegetables):
    vegetable = input("Enter vegetable name: ")
    if vegetable in vegetables:
        del vegetables[vegetable]
        print(f"{vegetable} has been deleted from the list of vegetables")
    else:
        print(f"{vegetable} is not in the list of vegetables")

def save_vegetables(vegetables):
    with open("vegetables.dat", "wb") as file:
        pickle.dump(vegetables, file)

def load_vegetables():
    try:
        with open("vegetables.dat", "rb") as file:
            vegetables = pickle.load(file)
    except FileNotFoundError:
        vegetables = {}
    return vegetables

def main():
    vegetables = load_vegetables()
    while True:
        display_menu()
        display_vegetables(vegetables)
        print("\n1. Add a new vegetable and price")
        print("2. Change the price of an existing vegetable")
        print("3. Delete an existing vegetable and price")
        print("4. Save vegetables and exit\n")
        choice = input("Enter choice: ")
        if choice == "1":
            add_vegetable(vegetables)
        elif choice == "2":
            change_vegetable_price(vegetables)
        elif choice == "3":
            delete_vegetable(vegetables)
        elif choice == "4":
            save_vegetables(vegetables)
            print("Vegetables have been saved to vegetables.dat")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
