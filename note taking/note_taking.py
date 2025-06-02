#functional note taking app

import os


filenames=[]
def show_menu():
    print(""" 
_______________Note Taking Program_________________
          1)Create a new Note
          2)list all notes
          3)Append on existing note
          4)delete note
          5)read content
          6)exit
     
 """)
    
def create_note():
    while True:

        FILE_NAME=input("enter Note Name:")
        file_name=FILE_NAME +".txt"

        try:
            with open("filenames.txt","r") as name:
                filenames=[line.strip() for line in name.readlines()]
        except FileNotFoundError:
            filenames=[]
                



        
        if FILE_NAME in filenames:
            print("File already exists.")
            choice=input("do you want to replace the current file(all previous data will be lost)-[y/n]").lower()

            if choice=="y":
                break
            else:
                print("enter new name:")
                continue
        else:
            break

    if FILE_NAME not in filenames:

        with open("filenames.txt","a") as names:
            names.write(f"{FILE_NAME}\n")



    with open(file_name,"w") as file:
        content=input("Start Content\n")
        file.write(f"{content}\n")
        



def list_notes():
    with open("filenames.txt",'r') as f:
        content=f.read()

        print(content)
    

def append():


    filename=input("enter the file name to open:")

    Filename=filename+".txt"

    with open("filenames.txt","r") as name:
            
        try:
            filenames=[line.strip() for line in name.readlines()]
        except FileNotFoundError:
            filenames=[]
    
    if filename in filenames:
    

        with open(Filename,"a") as file:
            content=input("enter content:\n")
            file.write(content)
    else:
        print("no such files")

def delete():
    filename = input("Enter the file name to delete:").strip()
    note_file = filename + ".txt"

    if os.path.exists(note_file):
        os.remove(note_file)

    try:
        with open("filenames.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    with open("filenames.txt", "w") as ff:
        for line in lines:
            if line.strip() != filename:
                ff.write(line)

    print(f"Note '{filename}' deleted (if it existed).")
    
        
    
def read():
    filename=input("enter the file name to open:")

    Filename=filename+".txt"

    with open("filenames.txt","r") as name:
            
        try:
            filenames=[line.strip() for line in name.readlines()]
        except FileNotFoundError:
            filenames=[]
    
    if filename in filenames:
    

        with open(Filename,"r") as file:
            content=file.read()
            print(content)
    else:
        print("no such files")



def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            create_note()
        elif choice == "2":
            list_notes()
        elif choice == "3":
            append()
        elif choice == "4":
            delete()
        elif choice== "5":
            read()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
    
