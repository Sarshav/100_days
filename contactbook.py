# learning dictionary

contact_book={}

def show_menu():
    print(""" 
______________Contact book___________
          
    1. add contact
    2. view contacts
    3.search contact
    4.edit contact
    5.delete contact
    6.exit

    """)

def add_contact():
    name=input("Name:")
    email=input("Email:")
    phone_no=input("Phone Number:")

    contact_book[name]={"Email":email,"Phone_number":phone_no}

def view_contacts():
    print("___________contact list____________")
    for name,details in contact_book.items():

        print(f"Name:{name}")
        print(f"Email:{details["Email"]}")
        print(f"Phone Number:{details["Phone_number"]}")
        print("\n")
def search_contacts():
    search_name=input("enter name:").lower()
    found=False

    for name,details in contact_book.items():
       

        if name.lower()==search_name:
            print(f"Name:{name}")
            print(f"Email:{details["Email"]}")
            print(f"Phone Number:{details["Phone_number"]}")
            found=True
            break

    if not found:
        print("NO DATA FOUND")

def edit_contacts():
    edit_name=input("enter name:").lower()
    found=False
    for name,details in contact_book.items():
       

        if name.lower()==edit_name:
            print(f"Name:{name}")
            print(f"Email:{details["Email"]}")
            print(f"Phone Number:{details["Phone_number"]}")
            print("")

            new_email=input("enter new email")
            details["Email"]=new_email
            new_phone=input("enter new phone no")
            details["Phone_number"]=new_phone
            print(" ")

            print("New data")
            print(f"Name:{name}")
            print(f"Email:{details["Email"]}")
            print(f"Phone Number:{details["Phone_number"]}")


            found=True
            break
    if not found:
        print("no such User")

def delete_contact():
    del_name=input("enter user name to delete:").lower()
    found=False

    for name in contact_book:
        if del_name==name.lower():
            
            target=del_name
            found=True

    if not found:
        print("No such user")
    else:
        del contact_book[target]


def main():

    while True:
        show_menu()
        choice=input("enter choice:")

        if choice=="1":
            add_contact()
        elif choice=='2':
            view_contacts()
        elif choice=="3":
            search_contacts()
        elif choice=="4":
            edit_contacts()
        elif choice=="5":
            delete_contact()
        elif choice=="6":
            break
        else:
            print("invalid choicce!enter an valid choice")


main()







        




            

