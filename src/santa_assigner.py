import random
from src.utils import shuffle_list

class SantaAssign:
    def __init__(self, employees, previousYearData):
        self.employees = employees
        self.previousYearData = previousYearData
        self.assignments = {}

    def assign(self):
        shuffled_employees = shuffle_list(self.employees)
        # print(shuffled_employees)
        for i, employee in enumerate(self.employees):
            # print("i value",i)
            # print("employyeee value",employee)
            updated_data = shuffled_employees[(i + 1) % len(shuffled_employees)]
            # print(updated_data)
            if (employee['email'] == updated_data['email'] or
                    self.previousYearData.get(employee['email']) == updated_data['email']):
                shuffled_employees = shuffle_list(self.employees)
                return self.assign() 

            self.assignments[employee['email']] = updated_data

        return self.assignments
