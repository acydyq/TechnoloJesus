class Project:
    def __init__(self, name, difficulty):
        """Initializes a project with a name, difficulty, and progress tracking."""
        self.name = name
        self.progress = 0
        self.difficulty = difficulty
        self.is_completed = False
        self.assigned_employees = []

    def work_on_project(self, productivity):
        """Increases project progress based on assigned employee productivity."""
        if not self.is_completed:
            self.progress += productivity / self.difficulty
            if self.progress >= 100:
                self.progress = 100
                self.is_completed = True
                print(f"Project '{self.name}' is completed!")

    def assign_employee(self, employee):
        """Assigns an employee to the project."""
        self.assigned_employees.append(employee)

    def __repr__(self):
        return f"{self.name} - Progress: {self.progress:.2f}% - {'Completed' if self.is_completed else 'In Progress'}"


class ProjectManager:
    def __init__(self):
        """Manages all ongoing and completed projects."""
        self.projects = []

    def start_project(self, name, difficulty=5):
        """Starts a new project with a given difficulty level (default 5)."""
        project = Project(name, difficulty)
        self.projects.append(project)
        print(f"Started project: {project}")

    def update_projects(self, total_productivity):
        """Updates all active projects based on team productivity."""
        for project in self.projects:
            if not project.is_completed:
                project.work_on_project(total_productivity)

    def get_active_projects(self):
        """Returns only active (unfinished) projects."""
        return [proj for proj in self.projects if not proj.is_completed]

    def assign_employee_to_project(self, employee, project_name):
        """Assigns an employee to a project by name."""
        project = next((p for p in self.projects if p.name == project_name), None)
        if project:
            project.assign_employee(employee)
            print(f"{employee.name} assigned to {project.name}")
        else:
            print(f"Project '{project_name}' not found.")

# Test project system
if __name__ == "__main__":
    manager = ProjectManager()
    manager.start_project("AI Chatbot", difficulty=8)
    manager.start_project("Mobile App", difficulty=5)

    print(manager.get_active_projects())
