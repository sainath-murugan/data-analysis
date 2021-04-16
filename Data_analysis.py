class HospitalManagement:

    def __init__(self, list_of_heart_patient=None, list_of_lung_patient=None, list_of_kidney_patient=None):
        self.list_of_heart_patient = list_of_heart_patient
        self.list_of_lung_patient = list_of_lung_patient
        self.list_of_kidney_patient = list_of_kidney_patient

    @classmethod
    def heart_patients(cls):
        list_of_heart_patient = {
            "Ajay": ["ajay", "10-04-2000", 20, "Male", 3456345987, "Tirunelveli district, Tamil Nadu, India", 12300,
                     "Cardiac failure", "critical, under treatment", "Benazepril, Captropil, Fosinopril", 2],
            "Priya": ["priya", "13-05-1996", 24, "Female", 1947504745, "Chennai-avadi, Tamil Nadu, India", 12301,
                     "Pericardial Disease", "Recovering, under treatment", "Lisinopril. Moexipril", 1],
            "Ravi": ["Ravi", "20-07-1990", 30, "Male", 466784567, "Salem, Tamil Nadu, India", 12302,
                     "Heart Arrhythimas", "Ready to discharge", "Captropil, Fosinopril", 1]
          }
        return cls(list_of_heart_patient)

    @classmethod
    def lung_patients(cls):
        list_of_lung_patient = {
            "Kajal": ["Kajal", "6-09-1999", 21, "Female", 3456783456, "Banda, Mumbai, India", 12400,
                      "Tuberclosis", "critical, under treatment", "Tardetox, Prevnar", "no operation have done"],
            "Hari": ["Hari", "6-08-1880", 41, "Male", 5673496548, "Chennai-manali, Tamil Nadu, India", 12401,
                     "Asthma", "Recovering, under treatment", "leukemias", 1],
            "Arjun": ["Arjun", "20-07-1995", 25, "male", 5673497824, "thanjavur, Tamil Nadu, India", 12402,
                      "COPD", "Ready to discharge", "pneumoconoal", 1]
          }
        return cls(None, list_of_lung_patient)

    @classmethod
    def kidney_patients(cls):
        list_of_kidney_patient = {
            "Sharmila": ["Sharmila", "6-09-1998", 22, "Female", 9076458923, "Kollam, Kerela, India", 12500,
                         "Nephrotoxicity", "critical, under treatment", "co-trimoxazole", "no operation have done"],
            "Aravind": ["Aravind", "8-07-1995", 25, "Male", 5445762398, "Chennai-paalpanna, Tamil Nadu, India", 12501,
                        "Lobar Nephronia", "Recovering, under treatment", "cyclophoshamide", 1],
            "Xavier": ["Adenine", "20-07-2002", 19, "Male", 907528756, "kaniyaKumari, Tamil Nadu, India", 12502,
                       "COPD", "Ready to discharge", "sirolimus", 1]
          }
        return cls(None, None, list_of_kidney_patient)

    def sort_heart_patients(self):
        while True:
            heart_patient_list = input("\nThere are 3 heart patients,"
                                       "\n 1.Ajay"
                                       "\n 2.Priya"
                                       "\n 3.Ravi"
                                       "\n enter the name of the patient you are looking for\n\n")

            if heart_patient_list in ["Ajay", "Priya", "Ravi"]:
                print(f"Name: {self.list_of_heart_patient[heart_patient_list][0]}\n"
                      f"Date of Birth: {self.list_of_heart_patient[heart_patient_list][1]}\n"
                      f"Age: {self.list_of_heart_patient[heart_patient_list][2]}\n"
                      f"Phone number: {self.list_of_heart_patient[heart_patient_list][4]}\n"
                      f"Address: {self.list_of_heart_patient[heart_patient_list][5]}\n"
                      f"Patient ID: {self.list_of_heart_patient[heart_patient_list][6]}\n"
                      f"Suffering from: {self.list_of_heart_patient[heart_patient_list][7]}\n"
                      f"Patient Status: {self.list_of_heart_patient[heart_patient_list][8]}\n"
                      f"Medicine: {self.list_of_heart_patient[heart_patient_list][9]}\n"
                      f"number of operation done: {self.list_of_heart_patient[heart_patient_list][10]}")
                break
            else:
                print("you have entered wrong name, enter the name with correct spelling\n\n")
                continue

    def sort_lung_patients(self):
        while True:
            lung_patient_list = input("\nThere are 3 lung patients,"
                                      "\n 1.Kajal"
                                      "\n 2.Hari"
                                      "\n 3.Arjun"
                                      "\n enter the name of the patient you are looking for\n\n")

            if lung_patient_list in ["Kajal", "Hari", "Arjun"]:
                print(f"Name: {self.list_of_lung_patient[lung_patient_list][0]}\n"
                      f"Date of Birth: {self.list_of_lung_patient[lung_patient_list][1]}\n"
                      f"Age: {self.list_of_lung_patient[lung_patient_list][2]}\n"
                      f"Phone number: {self.list_of_lung_patient[lung_patient_list][4]}\n"
                      f"Address: {self.list_of_lung_patient[lung_patient_list][5]}\n"
                      f"Patient ID: {self.list_of_lung_patient[lung_patient_list][6]}\n"
                      f"Suffering from: {self.list_of_lung_patient[lung_patient_list][7]}\n"
                      f"Patient Status: {self.list_of_lung_patient[lung_patient_list][8]}\n"
                      f"Medicine: {self.list_of_lung_patient[lung_patient_list][9]}\n"
                      f"number of operation done: {self.list_of_lung_patient[lung_patient_list][10]}")
                break
            else:
                print("you have entered wrong name, enter the name with correct spelling\n\n")
                continue

    def sort_kidney_patients(self):
        while True:
            kidney_patient_list = input("\nThere are 3 kidney patients,"
                                        "\n 1.Sharmila"
                                        "\n 2.Aravind"
                                        "\n 3.Xavier"
                                        "\n enter the name of the patient you are looking for\n\n")

            if kidney_patient_list in ["Sharmila", "Aravind", "Xavier"]:
                print(f"Name: {self.list_of_kidney_patient[kidney_patient_list][0]}\n"
                      f"Date of Birth: {self.list_of_kidney_patient[kidney_patient_list][1]}\n"
                      f"Age: {self.list_of_kidney_patient[kidney_patient_list][2]}\n"
                      f"Phone number: {self.list_of_kidney_patient[kidney_patient_list][4]}\n"
                      f"Address: {self.list_of_kidney_patient[kidney_patient_list][5]}\n"
                      f"Patient ID: {self.list_of_kidney_patient[kidney_patient_list][6]}\n"
                      f"Suffering from: {self.list_of_kidney_patient[kidney_patient_list][7]}\n"
                      f"Patient Status: {self.list_of_kidney_patient[kidney_patient_list][8]}\n"
                      f"Medicine: {self.list_of_kidney_patient[kidney_patient_list][9]}\n"
                      f"number of operation done: {self.list_of_kidney_patient[kidney_patient_list][10]}")
                break
            else:
                print("you have entered wrong name, enter the name with correct spelling\n\n")
                continue

    @staticmethod
    def total_no_of_patient():
        print("Total number of patient:\n"
              "Heart Patients: 3\n"
              "Lung Patients: 3\n"
              "Kidney Patients: 3")



obj = HospitalManagement()

username = input("please enter the username\n")  # username == admin
login = input("enter the password\n")  # password == admin
if username == "admin" and login == "admin":
    print("you are logged in successfully\n\n")
    while True:
        option = int(input("what are you looking for, Please enter the option number:"
                       "\n 1. To check the heart patient"
                       "\n 2. To check lung cancer patient"
                       "\n 3. To check kidney patient"
                       "\n 4. Total number of patients\n"))

        if option is 1:
            obj.heart_patients().sort_heart_patients()
            break
        elif option is 2:
            obj.lung_patients().sort_lung_patients()
            break
        elif option is 3:
            obj.kidney_patients().sort_kidney_patients()
            break
        elif option is 4:
            obj.total_no_of_patient()
            break
        else:
            print("please enter a valid option. option should be in number\n\n")
            continue


elif username != "admin" and login != "admin":
    print("Both username and password is wrong, enter the correct password and username")
elif username != "admin":
    print("your username is wrong, please enter correct username")
elif login != "admin":
    print("your password is wrong,  please enter correct password")
