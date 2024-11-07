import csv

class Output:
    def __init__(self, outputFileName):
        self.outputFileName = outputFileName

    def write_assignments(self, employees, assignments):
        with open(self.outputFileName, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Employee_Name', 'Employee_EmailID', 'Secret_Child_Name', 'Secret_Child_EmailID'])
            for employee in employees:
                child = assignments[employee['email']]
                writer.writerow([employee['name'], employee['email'], child['name'], child['email']])
