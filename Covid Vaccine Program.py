def mainMenu():
    print("---REGISTER NOW FOR VACCINATION TODAY---", "\n")
    while True:
        vacCenter = []
        choice = input("Please choose your vaccination center: VC1 or VC2. ")
        if choice in ["VC1", "VC2"]:
            dos = input("Before we proceed, have you taken the first dosage of any vaccine? y/n ")
            if dos == 'y':
                print("Sorry, you are not eligible for registering. New patient registration"
                      " can be only done once that is before the first dosage of vaccination.", "\n")
            elif dos == 'n':
                print("Great, let's get you registered up!\n")
                vacCenter.append(choice)
                '''stringFromList = ", ".join(vacCenter)
                with open("patients.txt", "a") as f:
                    f.write(stringFromList)'''
                with open("patients.txt") as f:
                    lines = ", ".join(vacCenter).splitlines()
                with open("patients.txt", "a") as f:
                    for line in lines:
                        f.write(line + ", ")
                    break
            else:
                print("Invalid choice. Please try again.", "\n")
        else:
            print("Invalid choice. Please make sure you have enter 'VC1' or 'VC2'.", "\n")
    return


mainMenu()


def patientDetails():
    while True:
        patients = []
        medHistory = []
        print("Notice: All fields are required, except for the ones marked as optional."
              " This section is related to your personal details.")
        while True:
            name = input("Enter your full name: ")
            if name.replace(" ", "").isalpha():
                break
            else:
                print("Invalid input. Please try again.")
        while True:
            nric = input("Enter your NRIC number: (eg: 012345-12-4567) ")
            if len(nric) == 14 and "-":
                break
            else:
                print("Invalid input. Please follow the format given.")

        age = input("Enter your age: ")
        email = input("Enter your email address: ")
        while True:
            contact = str(input("Enter your contact number: (eg: 0123456789) "))
            if contact.isnumeric():
                break
            else:
                print("Invalid input. Please follow the format given.")

        print("\nThis section is related to your health, ***Optional**")
        medical = input("Please state your medical history. ")
        blood = input("Blood group: ")
        weight = input("Weight(kg): ")
        height = input("Height(cm): ")
        patients.append(name)
        patients.append(nric)
        patients.append(age)
        patients.append(email)
        patients.append(contact)
        medHistory.append(medical)
        medHistory.append(blood)
        medHistory.append(weight)
        medHistory.append(height)

        print("Based on your age, these are the vaccines that you are eligible to register. ")
        if age >= '12':
            AF = print("Vaccine Code: AF    Dosage Required: 2      "
                       "Interval Between Doses: 2 weeks (or 14 days)")
            DM = print("Vaccine Code: DM    Dosage Required: 2      "
                       "Interval Between Doses: 4 weeks (or 28 days)")
            if age >= '18':
                BV = print("Vaccine Code: BV    Dosage Required: 2      "
                           "Interval Between Doses: 3 weeks (or 21 days)")
                EC = print("Vaccine Code: EC    Dosage Required: 1      ")
            if age <= '45':
                CZ = print("Vaccine Code: CZ    Dosage Required: 2      "
                           "Interval Between Doses: 3 weeks (or 21 days)")
        else:
            print("You are not eligible to take the vaccine.")

        while True:
            vac_choice = []
            vaccine = input("Enter your choice of vaccine: ")
            if vaccine in ["AF", "BV", "CZ", "DM", "EC"]:
                vac_choice.append(vaccine)
                print("You have chosen", vaccine, "as your vaccine.")
                break
            else:
                print("Invalid choice. Please try again.")

        print("Congratulations,you have been registered as a patient!")
        id = vaccine + str(nric[10:14] + ", ")
        print("This is your unique ID: ", id)
        patients.append(id)
        string = ", ".join(patients)
        string2 = ", ".join(medHistory)
        string3 = ", ".join(vac_choice)
        with open("patients.txt", "a") as f:
            f.write(string3 + ", ")
            f.write(string)
            f.write(string2 + "\n")
        return


patientDetails()
