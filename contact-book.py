def main():
    class ContactBook:
        contact_dict = {}
        total_contacts = 0

        @staticmethod
        def welcome():
            print('Welcome to Contact Book')
            print()

        def menu(self):
            print('0. Total Number of Contacts')
            print('1. Create Contact')
            print('2. View Contacts')
            print('3. Update Contact')
            print('4. Search Contact')
            print('5. Delete Contact')
            print('6. Exit')
            try:
                choice = int(input('Choose: '))
                return choice
            except ValueError:
                print('Invalid input. Please enter a number.')
                return -1

        def total_number_contacts(self):
            if ContactBook.total_contacts == 0:
                print('No contacts found')
            else:
                print('Total Contacts:', ContactBook.total_contacts)
            print('*******************************')

        def creating_contact(self):
            try:
                name = input('Enter Contact Name: ').lower()
                if name in ContactBook.contact_dict:
                    print(f'Contact with the name "{name}" already exists.')
                else:
                    age = int(input('Enter Age: '))
                    email = input('Enter Email: ')
                    phone_number = input('Enter Phone Number: ')
                    is_fav = input('Is Contact Favorite (y/n): ').lower()
                    favorite = True if is_fav == 'y' else False
                    ContactBook.contact_dict[name] = {
                        'Age': age,
                        'Email': email,
                        'Phone Number': phone_number,
                        'Favorite': favorite
                    }
                    ContactBook.total_contacts += 1
                    print('Contact Saved Successfully!')
            except Exception as e:
                print(f"Error: {e}")
            print('************************************************')

        def view_contact(self):
            if ContactBook.total_contacts == 0:
                print('No Records Found')
            else:
                for name, info in ContactBook.contact_dict.items():
                    print(f'{name} - {info}')
            print('*******************************************')

        def update_contact(self):
            try:
                name = input('Enter Contact Name to Update: ').lower()
                if name not in ContactBook.contact_dict:
                    print(f'Contact with the name "{name}" does not exist.')
                else:
                    age = int(input('Enter Age: '))
                    email = input('Enter Email: ')
                    phone_number = input('Enter Phone Number: ')
                    is_fav = input('Is Contact Favorite (y/n): ').lower()
                    favorite = True if is_fav == 'y' else False
                    ContactBook.contact_dict[name] = {
                        'Age': age,
                        'Email': email,
                        'Phone Number': phone_number,
                        'Favorite': favorite
                    }
                    print('Contact Updated Successfully')
            except Exception as e:
                print(f"Error: {e}")
            print('*******************************************')

        def search_contact(self):
            name = input('Enter name to search: ').lower()
            if name not in ContactBook.contact_dict:
                print('No Record Found')
            else:
                s_contact = ContactBook.contact_dict[name]
                print(f'Contact Found - {name}')
                for attribute, value in s_contact.items():
                    print(f'{attribute} - {value}')
            print('******************************************')

        def delete_contact(self):
            try:
                name = input('Enter Contact Name to Delete: ').lower()
                if name not in ContactBook.contact_dict:
                    print(f'No contact found with the name "{name}"')
                else:
                    del ContactBook.contact_dict[name]
                    ContactBook.total_contacts -= 1
                    print(f'Contact "{name}" deleted successfully.')
            except Exception as e:
                print(f"Error: {e}")
            print('***************************************')

    # Start the program
    ContactBook.welcome()
    my_contact_book = ContactBook()

    while True:
        try:
            result = my_contact_book.menu()
            if result == 0:
                my_contact_book.total_number_contacts()
            elif result == 1:
                my_contact_book.creating_contact()
            elif result == 2:
                my_contact_book.view_contact()
            elif result == 3:
                my_contact_book.update_contact()
            elif result == 4:
                my_contact_book.search_contact()
            elif result == 5:
                my_contact_book.delete_contact()
            elif result == 6:
                print("Exiting Contact Book. Goodbye!")
                break
            else:
                print('Please choose a valid number from the menu.')
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
