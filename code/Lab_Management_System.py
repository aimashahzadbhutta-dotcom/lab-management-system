import json
import csv

def main():
    count, limit = 0, 3
    password = input("Set your password: ").capitalize()
    username = input("Set your username: ").capitalize()
    while count != limit:
        count += 1
        Verify_password = input("Verify your password: ").capitalize()
        Verify_username = input("Verify your username: ").capitalize()
        if Verify_password != password and Verify_username == username:
            print(f"Count {count}, Attempt Failed!\nIncorrect password")
        elif Verify_password == password and Verify_username != username:
            print(f"Count {count}, Attempt Failed!\nIncorrect username")
        else:
            print("Attempt Successful!\nYou are logged in.")
            break
    menu()

def menu():
    print("Here is your menu:")
    Menu = ["Add patient", "Add experiment", "View all drugs", "Search Drug", "Quit"]
    for e, content in enumerate(Menu, start=1):
        print(f"{e}. {content}")
    with open ('drugs.json', 'r') as f:
        drugs = json.load(f)
    while True:
        try:
            menu = int(input("Enter a desired number(1 - 5): "))
        except ValueError:
            print("You can only use numbers")
        else:
            if menu < 1 or menu > 5:
                print("Use a number between 1 - 5")
            elif menu == 5:
                print("You are logged out!")
                break
            elif menu == 3:
                print("Following is the list of all the drugs available in the database:")
                for e, drug in enumerate(drugs, start=1):
                    print(f"\n{e}. {drug['generic_name']}")

            elif menu == 4:
                while True:
                    search_drug = input("Enter the name of the drug you are searcing for(Q to Quit): ").capitalize()
                    if search_drug == "Q":
                        print("\n You can select any of the following options: ")
                        for e, content in enumerate(Menu, start=1):
                            print(f"{e}. {content}")
                        print("\n")
                        break
                    for drug in drugs:
                        if search_drug.capitalize() == drug['generic_name'].capitalize():
                            print(drug)
                            break
                    else:
                        print("Sorry, information about this drug is not available!")
            elif menu == 1:
                new_patient = input("Enter the name of new patient: ").title()
                while True:
                    try:
                        new_patient_age = int(input("Enter Age of the patient: "))
                    except ValueError:
                        print("Use numbers!")
                    else:
                        break
                new_patient_report = input("Enter result of the patient's report: ").capitalize()
                new_patient_data = {
                    "Names" : new_patient,
                    "Ages" : new_patient_age,
                    "Reports" : new_patient_report
                }

                fields = ['Names', 'Ages', 'Reports']
                with open('patients.csv', 'a', newline="") as f:
                    csv_writer = csv.DictWriter(f, fieldnames = fields)
                    csv_writer.writeheader()
                    csv_writer.writerow(new_patient_data)
                show_list = input("Do you want to see the list of all patients? (y/n)").lower()
                while True:
                    if show_list == 'y':
                        with open('patients.csv', 'r') as f:
                            csv_reader = csv.DictReader(f)
                            fields = next(csv_reader)
                            print(fields)
                            for row in csv_reader:
                                print(row)
                    break

            elif menu == 2:
                exp = input("Enter the name of experiment: ").capitalize()
                result = input("Enter the result of experiment(Passed/Failed): ").capitalize()
                append = f"{exp} == {result}"
                with open("experiments.txt", "a") as f:
                    new_line = f.write(str(append))
                show_list = input("Do you want to see the list of all experiments? (y/n)").lower()
                while True:
                    if show_list == 'y':
                        with open('experiments.txt', 'r') as f:
                            read_file = f.read()
                            print(read_file)
                    break
                
            else:
                print("This feature is not yet available")

main()
    
 