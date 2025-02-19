import pandas as pd
from fpdf import FPDF
import json
import extList 

DATA_FILE_PATH="Test.json"


def generate_pdf():
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    try:
        with open(DATA_FILE_PATH, "r", encoding="utf-8") as data_file:
            people_data = json.load(data_file)

        pdf.cell(200, 10, txt="People Report", ln=True, align="C")
        pdf.ln(10)  # Add space

        for i in range(len(people_data["Name"])):
            pdf.cell(200, 10, txt=f"{people_data['Name'][i]} {people_data['Surname'][i]}, Age: {people_data['Age'][i]}", ln=True)

        pdf.output("people_report.pdf")
        print("PDF report generated successfully!")

    except Exception as e:
        print(f"Error generating PDF: {e}")


def save_json_data(data):
        # Load the entire JSON data
        with open(DATA_FILE_PATH, mode="r+", encoding="utf-8") as data_file:
            
            try:
                all_data = json.load(data_file)
            except json.JSONDecodeError:
                all_data = {"Name": [], "Surname": [], "Age": []}  # Empty structure if file is empty

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
    try:
        with open(DATA_FILE_PATH, "r", encoding="utf-8") as data_file:
            people_data = json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        people_data = {"Name": [], "Surname": [], "Age": []}  # Default structure

if __name__=="__main__":
    while True:
        df = pd.DataFrame(dict(people_data))
        print("Insert command:")
        command=input()
        match command:
            case "input":
                add_person()
            case "pdf":
                generate_pdf()
                print("File saved!")
            case "csv":
                df.to_csv("people.csv")
                print("File saved!")
            case "excel":
                df.to_excel("people.xlsx",sheet_name="marostica")
                print("File saved!")
            case "data":
                print(df)
            case "exit":
                break
        print()
