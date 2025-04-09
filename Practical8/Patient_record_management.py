class patients:
    def __init__(self, patient_name, age, latest_admission_date, medical_history):
        self.patient_name = patient_name
        self.age = age
        self.latest_admission_date = latest_admission_date
        self.medical_history = medical_history

    def print_details(self):
        print(f"Patient Name: {self.patient_name}, Age: {self.age}, "
              f"Date of Latest Admission: {self.latest_admission_date}, "
              f"Medical History: {self.medical_history}")

tested_patient = patients("John Doe", 35, "2025-04-01", "High blood pressure")
tested_patient.print_details()

a=input("Patient's name")
b=int(input("Patient's age"))
c=input("Patent's latest admission data")
d=input("Patient's medical history")
patent1=patients(a,b,c,d)
patent1.print_details()