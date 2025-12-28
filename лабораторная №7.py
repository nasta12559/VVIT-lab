class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.id = emp_id

    def get_info(self):
        return f"Сотрудник: {self.name}, идентификатор: {self.id}"


class Manager(Employee):
    def __init__(self, name, emp_id, department):
        # Замечание: удаляем вызов super() и явно обращаемся к Employee
        Employee.__init__(self, name, emp_id)
        self.department = department

    def get_info(self):
        return (
            f"Менеджер: {self.name}, "
            f"идентификатор: {self.id}, "
            f"отдел: {self.department}"
        )

    def manage_project(self):
        return f"{self.name} управляет проектом в отделе «{self.department}»"


class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        Employee.__init__(self, name, emp_id)
        self.specialization = specialization

    def get_info(self):
        return (
            f"Техник: {self.name}, "
            f"идентификатор: {self.id}, "
            f"специализация: {self.specialization}"
        )

    def perform_maintenance(self):
        return (
            f"{self.name} выполняет техническое обслуживание "
            f"(специализация: {self.specialization})"
        )


class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Manager.__init__(self, name, emp_id, department)
        Technician.__init__(self, name, emp_id, specialization)
        self.specialization = specialization
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def perform_maintenance(self):
        return (
            f"{self.name} организует и контролирует технические работы "
            f"по направлению «{self.specialization}»"
        )

    def get_team_info(self):
        if not self.team:
            return "Команда ещё не сформирована."

        result = "Состав команды менеджера:\n"
        for emp in self.team:
            result += f"- {emp.get_info()}\n"
        return result


if __name__ == "__main__":
    print("Демонстрация работы системы управления сотрудниками\n")

    employee = Employee("Иван", 1)
    manager = Manager("Анна", 2, "Финансовый отдел")
    technician = Technician("Сергей", 3, "Сетевое оборудование")
    tech_manager = TechManager("Ольга", 4, "Отдел разработки", "Программное обеспечение")

    print(employee.get_info())
    print(manager.get_info())
    print(manager.manage_project())
    print(technician.get_info())
    print(technician.perform_maintenance())

    tech_manager.add_employee(employee)
    tech_manager.add_employee(technician)

    print()
    print(tech_manager.manage_project())
    print(tech_manager.perform_maintenance())
    print(tech_manager.get_team_info())