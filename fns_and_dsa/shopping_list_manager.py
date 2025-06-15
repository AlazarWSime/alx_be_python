def display_menu():

    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
                      
    while True:
        display_menu()
        choice = input("Enter your choice input as a number: ")

        if choice == '1':
           item = input("what item do you want to add: ")
           shopping_list.append(item) 
           pass
        elif choice == '2':
           item = input("what item do you want to remove: ")
           if item in shopping_list:
                  shopping_list.remove(item)
           else:
               print("The item you want to remove doesn't exist in your shopping list!")
           pass
        elif choice == '3':
            print(f"Your shoping List is: {shopping_list}")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()