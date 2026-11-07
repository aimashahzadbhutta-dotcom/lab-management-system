import csv

patients_data = [
    {'Names' : 'Amara', 'Ages' : 48, 'Report' : "Positive"}, 
    {'Names' : 'Memona', 'Ages' : 32, 'Report' : "Positive"}, 
    {'Names' : 'Asif', 'Ages' : 22, 'Report' : "Negative"}, 
    {'Names' : 'Raza', 'Ages' : 49, 'Report' : "Positive"}
]

fields = ['Names', 'Ages', 'Report']

with open ('patients.csv', 'a', newline='') as f:
    csv_dictwriter = csv.DictWriter(f, fieldnames = fields)
    csv_dictwriter.writeheader()
    csv_dictwriter.writerows(patients_data)