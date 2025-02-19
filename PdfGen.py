import pandas as pd
import fpdf as pdf
import json
import extList 
from os import system, name

# define our clear function
def clear_terminal():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

DATA_FILE_PATH="Test.json"

def save_json_data(data):
        # Load the entire JSON data
        with open(DATA_FILE_PATH, mode="r+", encoding="utf-8") as data_file:
            all_data = json.load(data_file)
            all_data.update(data)  # Update or add data
            data_file.seek(0)  # Move the file pointer to the beginning
            json.dump(all_data, data_file, indent=4)  # Save updated data
            data_file.truncate()  # Remove any leftover data in the file

def add_person():
    print("Please enter a Name: ")
    people_data["Name"].append(input())
    print("Please enter a Surname: ")
    people_data["Surname"].append(input())
    print("Please enter an Age: ")
    people_data["Age"].append(input())
    clear_terminal()
    print("Name = ",extList.GetLast(people_data["Name"]))
    print("Surname = ",extList.GetLast(people_data["Surname"]))
    print("Age = ",extList.GetLast(people_data["Age"]))
    print("Please confirm the data are correct (Y/N) :")
    
    user_command=input()
    match str(user_command).upper():
        case "Y":
            save_json_data(people_data)
            print ("The data have been saved!")
            return
    print("The operation has been canceled!")

command=""

with open(DATA_FILE_PATH,mode="r", encoding="utf-8") as data_file:
    people_data=json.load(data_file)

if __name__=="__main__":
    while(True):
        df = pd.DataFrame(dict(people_data))
        print("Insert command:")
        command=input()
        match command:
            case "input":
                add_person()
            case "pdf":
                clear_terminal()
                #todo create a pdf with fpdf
            case "csv":
                clear_terminal()
                print(df)
                df.to_csv("people.csv")
            case "excel":
                clear_terminal()
                print(df)
                df.to_excel("people.xlsx",sheet_name="marostica")
            case "exit":
                break
        print()
