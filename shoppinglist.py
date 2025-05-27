##shoping list

shopping_list=[]
def show_menu():
    print("""----shopping program----- 
    1-add item
    2-remove item
    3-list items
    4-clear list
    5-exit
    
          """)

while True:
    show_menu()

    choice=int(input("Enter your choice:"))

    match(choice):
        case 1:
            
            n=int(input("number of items u want to add:"))
            for i in range(n):
                item=input(f"enter item no {i+1}:").lower()
                shopping_list.append(item)
        
        case 2:

            removing_item=input("enter name of item to remove").lower()
            try:
                shopping_list.remove(removing_item)
            
            except ValueError:
                print("no such item in list")

        case 3:
            for index,item in enumerate(shopping_list):
                print(f"{index+1}. {item}")
        
        case 4:
            shopping_list.clear()
            print("list cleared")

        case 5:
            break

 




