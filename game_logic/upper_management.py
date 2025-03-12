class UpperManagement:
    def __init__(self, employee_manager):
        """Tracks all employees at a high level."""
        self.employee_manager = employee_manager

    def get_employee_summary(self):
        """Generates a summary of all employees."""
        summary = []
        for emp in self.employee_manager.employees:
            summary.append({
                "Name": emp.name,
                "Role": emp.role,
                "Hunger": random.randint(0, 100),
                "Fatigue": random.randint(0, 100),
                "Brodom": random.randint(0, 100),
                "Stress": random.randint(0, 100),
                "Last Completed Task": "Completed project X",
                "Current Task": "Debugging feature Y"
            })
        return summary

    def print_employee_list(self):
        """Displays all employees' needs and work history."""
        for emp in self.get_employee_summary():
            print(f"👨‍💻 {emp['Name']} ({emp['Role']}) - Hunger: {emp['Hunger']} | Fatigue: {emp['Fatigue']} | Brodom: {emp['Brodom']}")
