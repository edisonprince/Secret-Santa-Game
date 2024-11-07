import csv

class DataLoader:
    def __init__(self, employeeData, previousYearData):
        self.employeeData = employeeData
        self.previousYearData = previousYearData

    def loadEmployee(self):
        employees = []
        with open(self.employeeData, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                employees.append({
                    'name': row['Employee_Name'],
                    'email': row['Employee_EmailID']
                })
        return employees

    def loadPreviousYearData(self):
        previousYearData = {}
        with open(self.previousYearData, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                previousYearData[row['Employee_EmailID']] = row['Secret_Child_EmailID']
        return previousYearData
