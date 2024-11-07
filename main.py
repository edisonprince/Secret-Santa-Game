import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_loader import DataLoader
from src.santa_assigner import SantaAssign
from src.output_writer import Output

def main():
    employeeData = 'data/Employee-List.csv'
    previousYearData = 'data/Secret-Santa-Game-Result-2023.csv'
    outputFileName = 'data/new_secret_santa_assignments.csv'

    data_loader = DataLoader(employeeData, previousYearData)
    employees = data_loader.loadEmployee()
    previousYearData = data_loader.loadPreviousYearData()
    santaAssign = SantaAssign(employees, previousYearData)
    assignments = santaAssign.assign()
    outputWritter = Output(outputFileName)
    outputWritter.write_assignments(employees, assignments)
    print(f"New Secret Santa assignments written to {outputFileName}")

if __name__ == "__main__":
    main()
