import json
from typing import Sequence, Optional

class Database:
    def __init__(self, file_name):
        self.file_name = file_name
        
    def get_data(self):
        try:
            with open(self.file_name, mode='r', encoding='UTF-8') as file:
                content = file.read()
                return json.loads(content)
        except FileNotFoundError:
            return None
        
    def set_data(self, data):
        json_data = json.dumps(data)
        with open(self.file_name, mode='w', encoding='UTF-8') as file:
            file.write(json_data)




class Employee:
    monthly_hour = 160
    # created_employees = []
    def __init__(self, name: str, age: int, salary: float, job: str, hours: int = 0):
        self.name = name
        self.age = age
        self.salary = salary
        self.job = job
        self.hours = hours
        # self.created_employees.append(self)
        
        
    def hourly_bill(self):
        return self.salary / self.monthly_hour
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
    def serialize(self):
        return {
            'name': self.name,
            'age': self.age,
            'salary': self.salary,
            'job': self.job,
            'hours': self.hours
        }

class Company:
    def __init__(self, name: str):
        self.name = name
        self.employees: list[Employee] = []
        self.database = Database(self.name.lower() + '_db.json')
        
    def add_employees(self, employees: Sequence[Employee]) -> None:
        for employee in employees:
            self.add_employee(employee)
        
    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)
        self.save()
        
    def remove_employee(self, employee: Employee) -> None:
        self.employees.remove(employee)
        self.save()
        
    def __len__(self):
        return len(self.employees)
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
    def get_monthly_salary(self) -> float:
        return sum([e.salary for e in self.employees])
    
    def get_average_salary(self) -> float:
        return self.get_monthly_salary() / len(self)
    
    def get_average_age(self) -> float:
        return sum([e.age for e in self.employees]) / len(self)
    
    def get_total_hours(self):
        return sum([e.hours for e in self.employees])
    
    def get_emplyee_by_name(self, name: str) -> Optional[Employee]:
        for e in self.employees:
            if e.name == name:
                return e
            
    def serialize(self):
        return [e.serialize() for e in self.employees]
    
    def save(self):
        self.database.set_data(self.serialize())
        
    def load(self):
        data = self.database.get_data()
        if data:
            for info in data:
                employee = Employee(
                    name=info['name'], salary=info['salary'], job=info['job'], age=info['age']
                )
                self.add_employee(employee)
                
            
class CompanyInteraction:
    def __init__(self, company):
        self.company: Company = company
        
    def ask_new_user(self):
        print('Write info of new user at below:')
        name = input('name: '.title())
        job = input('job: '.title())
        salary = float(input('salary: '.title()))
        age = int(input('age: '.title()))
        hours = int(input('hours: '.title()))
        new_employee = Employee(name=name, age=age, salary=salary, job=job, hours=hours)
        self.company.add_employee(new_employee)
        
    def show_company_info(self):
        print('{:<15} {:<25} {:<10} {:<10} {:<10}'.format('Name', 'Job', 'Salary', 'Age', 'Hours'))
        print('-' * 75)
        for e in self.company.employees:
            print('{:<15} {:<25} {:<10} {:<10} {:<10}'.format(
                e.name, e.job, e.salary, e.age, e.hours
            ))


if __name__ == '__main__':
    
    compar = Company('Compar')
    # compar.add_employees([employee1, employee2, employee3, employee4, employee5, employee6, employee7, employee8, employee9, employee10])


    # print(len(compar))
    # print(compar.get_monthly_salary())
    # print(compar.get_average_salary())
    # print(compar.get_average_age())
    # print(compar.get_total_hours())
    # print(employee1.serialize())
    # print(compar.serialize())
    
    # compar.save()
    
    compar.load()
    compar_interaction = CompanyInteraction(compar)
    # compar_interaction.ask_new_user()
    # print(compar.employees)
    
    compar_interaction.show_company_info()