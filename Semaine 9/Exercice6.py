from datetime import *

Citizens_Vaccine = {
    "Mason Brown" : [("Pfizer","22-03-2021"),("Pfizer","21-10-2021")],
    "Samantha Smith" : [("Already infected","21-05-2021"),("Pfizer","02-01-2021")],
    "John Doe" : [("Moderna","14-08-2021"),("Moderna","02-01-2022")],
    "Lucy Callahan" : [("Pfizer","14-08-2021"),("Pfizer","16-01-2022")],
    "James Smith" : [("Pfizer","14-08-2021")]
}

def add_citizen():
    Citizen = str(input("Enter the name of the citizen: "))
    if Citizen in Citizens_Vaccine:
        print("This citizen already has a vaccine")
    else:
        vaccines = []
        nb_shots = int(input("Enter the number of shots: "))
        for i in range(nb_shots):
            Vaccine = input("Enter the name of the vaccine: ")
            Date = input("Enter the date of the vaccine: ")
            vaccines.append((Vaccine,Date))
        Citizens_Vaccine[Citizen] = vaccines
        print("The citizen has been added to the list!")

# add_citizen()

def add_vaccine():
    Citizen = str(input("Enter the name of the citizen: "))
    if Citizen in Citizens_Vaccine:
        Vaccine = input("Enter the name of the vaccine: ")
        Date = input("Enter the date of the vaccine: ")
        Citizens_Vaccine[Citizen].append((Vaccine,Date))
        print("The vaccine has been added to the list!")
    else:
        print("This citizen does not exist")
    
# add_vaccine()

def verify_pass(Citizen):
    limit_date = date(2022,1,15)
    six_months = datetime.now() - timedelta(days=180)
    six_months.strftime("%Y-%m-%d")
    if Citizen in Citizens_Vaccine:
        last_vaccine = Citizens_Vaccine[Citizen][-1][1]
        d1,m1,y1 = last_vaccine.split("-")
        last_vaccine_date = date(int(y1),int(m1),int(d1))
        if len(Citizens_Vaccine[Citizen]) > 2:
            return True
        elif len(Citizens_Vaccine[Citizen]) < 3 and six_months.date() < last_vaccine_date:
            return True
        elif len(Citizens_Vaccine[Citizen]) == 2 and limit_date > last_vaccine_date:
            return True
        else:
            return False
    else:
        print("This citizen does not exist")

# Citizen = str(input("Enter the name of the citizen: "))
# ans = verify_pass()
# if ans:
#     print("The citizen have a valid pass")
# else:
#     print("The citizen does not have a valid pass")

def invalid_pass_list():
    for i in Citizens_Vaccine:
        if not verify_pass(i):
            print(i)

invalid_pass_list()