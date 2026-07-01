#9. Create a Patient Class
#Create a class named Patient with:
#- patient_name
#- doctor_name
#- bill_amount
#Create 5 patient objects and print their details.
class Patient:
    def __init__(self, patient_name, doctor_name, bill_amount):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.bill_amount = bill_amount
 
p1 = Patient("Alia", "Dr. Tina", 1500)
p2 = Patient("Neo", "Dr. Arie", 2200)
p3 = Patient("ria", "Dr. Nina", 800)
p4 = Patient("Sid", "Dr. Rao", 3000)
p5 = Patient("Vincy", "Dr. Iyer", 1200)
 
for p in [p1, p2, p3, p4, p5]:
    print(p.patient_name, p.doctor_name, p.bill_amount)