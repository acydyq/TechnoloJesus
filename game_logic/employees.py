import random

class Employee:
    def __init__(self, name, role, skill_level):
        """Initializes an employee with attributes, enthusiasm, performance tracking, and daily salary."""
        self.name = name
        self.role = role
        self.skill_level = skill_level
        self.happiness = 100  # Affects retention
        self.enthusiasm = 100  # Affects productivity
        self.assigned_project = None

        # Determine daily salary based on role
        if role == "Software Engineer":
            annual_salary = 103479  # Average annual salary in Austin, TX
        elif role == "Product Manager":
            annual_salary = 138647  # Average annual salary in Austin, TX
        else:
            annual_salary = 75000  # Default annual salary for other roles

        # Convert annual salary to daily salary (based on 260 workdays per year)
        self.daily_salary = annual_salary / 260

        # Performance tracking
        self.tasks_completed = 0
        self.total_productivity = 0
        self.days_worked = 0
        self.loyalty = 100  # Loyalty declines if morale is too low

    def work(self):
        """Reduces enthusiasm, contributes work, and tracks performance."""
        if self.assigned_project:
            self.enthusiasm -= random.randint(3, 7)
            self.enthusiasm = max(0, self.enthusiasm)

            productivity = (self.skill_level * (self.enthusiasm / 100)) * random.uniform(0.8, 1.2)
            self.total_productivity += productivity
            self.days_worked += 1

            self.assigned_project.work_on_project(productivity)

            if self.assigned_project.is_completed:
                self.tasks_completed += 1
                self.assigned_project = None  

    def assign_project(self, project):
        """Assigns an employee to a project."""
        self.assigned_project = project

    def restore_enthusiasm(self, amount):
        """Boosts enthusiasm (e.g., from recreation)."""
        self.enthusiasm = min(100, self.enthusiasm + amount)

    def update_happiness(self, change):
        """Adjusts morale and loyalty."""
        self.happiness = max(0, min(100, self.happiness + change))
        if self.happiness < 50:
            self.loyalty -= 5  

    def get_performance_review(self):
        """Generates a performance review based on work history."""
        avg_productivity = self.total_productivity / self.days_worked if self.days_worked > 0 else 0

        return {
            "Employee": self.name,
            "Tasks Completed": self.tasks_completed,
            "Avg Productivity": round(avg_productivity, 2),
            "Enthusiasm Level": self.enthusiasm,
            "Loyalty Score": self.loyalty,
        }

    def request_raise(self):
        """Determines if an employee will ask for a raise based on performance."""
        avg_productivity = self.total_productivity / self.days_worked if self.days_worked > 0 else 0
        if avg_productivity > 8 and self.loyalty > 70:
            raise_amount = self.daily_salary * 0.1  
            return True, raise_amount  
        return False, 0  

    def check_quitting(self):
        """Determines if the employee is likely to quit."""
        if self.loyalty < 30 and self.happiness < 40:
            print(f"{self.name} is considering quitting due to low morale!")
            if random.random() < 0.3:
                print(f"{self.name} has quit the company.")
                return True
        return False

    def __repr__(self):
        status = f"Working on: {self.assigned_project.name}" if self.assigned_project else "Unassigned"
        return f"{self.name} ({self.role}) - Skill: {self.skill_level} | Daily Salary: ${self.daily_salary:.2f} | Enthusiasm: {self.enthusiasm} | Happiness: {self.happiness} | Loyalty: {self.loyalty} | {status}"


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def hire_employee(self, name, role):
        """Hires a new employee with random skill level."""
        skill_level = random.randint(1, 10)
        new_employee = Employee(name, role, skill_level)
        self.employees.append(new_employee)
        print(f"Hired {new_employee}")

    def fire_employee(self, name):
        """Fires an employee by name."""
        self.employees = [emp for emp in self.employees if emp.name != name]
        print(f"{name} has been fired.")

    def assign_employee_to_project(self, employee_name, project):
        """Assigns an employee to a project."""
        for employee in self.employees:
            if employee.name == employee_name:
                employee.assign_project(project)
                print(f"{employee.name} is now working on {project.name}.")
                return
        print(f"Employee {employee_name} not found.")

    def calculate_total_daily_salary(self):
        """Returns the total daily salary expenses."""
        return sum(emp.daily_salary for emp in self.employees)

    def apply_recreation(self):
        """Boosts enthusiasm for employees and prevents burnout."""
        for employee in self.employees:
            if employee.enthusiasm < 80:
                employee.restore_enthusiasm(random.randint(10, 25))
        print("Employees participated in recreational activities, boosting enthusiasm!")

    def conduct_performance_reviews(self):
        """Conducts performance reviews, handles raise requests, and checks for quitting."""
        print("\n=== Employee Performance Reviews ===")
        employees_to_remove = []
        for employee in self.employees:
            review = employee.get_performance_review()
            print(review)

            # Handle Raise Requests
            wants_raise, raise_amount = employee.request_raise()
            if wants_raise:
                print(f"{employee.name} requests a raise of ${round(raise_amount, 2)}!")
                employee.daily_salary += raise_amount  

            # Handle Potential Quitting
            if employee.check_quitting():
                employees_to_remove.append(employee.name)

        # Remove employees who quit
        for emp_name in employees_to_remove:
            self.fire_employee(emp_name)

# Test raise and quitting system
if __name__ == "__main__":
    manager = EmployeeManager()
    from game_logic.projects import Project
    test_project = Project("Test AI App", difficulty=8)

    manager.hire_employee("Alice", "Software Engineer")
    manager.assign_employee_to_project("Alice", test_project)

    for day in range(10):
        print(f"\nDay {day + 1}:")
        for emp in manager.employees:
            emp.work()
        if day % 3 == 0:
            manager.apply_recreation()

    manager.conduct_performance_reviews()
