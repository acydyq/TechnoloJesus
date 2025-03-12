import random
from game_logic.employees import EmployeeManager
from game_logic.projects import ProjectManager
from game_logic.economy import Economy
from game_logic.social_media import SocialMedia
from game_logic.random_events import RandomEvents
from game_logic.rival_companies import RivalManager
from game_logic.user_data_sales import UserDataSales
from game_logic.crypto_scams import CryptoScams

class StartupSimulation:
    def __init__(self):
        """Initializes all core systems, including legitimate and shady business operations."""
        print("Debug: Initializing StartupSimulation...")
        self.economy = Economy()
        self.employee_manager = EmployeeManager()
        self.project_manager = ProjectManager()
        self.social_media = SocialMedia()
        self.random_events = RandomEvents()
        self.rival_manager = RivalManager()
        self.user_data_sales = UserDataSales()
        self.crypto_scams = CryptoScams()

    def hire_employee(self, name, role):
        """Hires an employee and deducts the first salary."""
        self.employee_manager.hire_employee(name, role)
        salary = self.employee_manager.calculate_total_daily_salary()
        self.economy.update_expenses("Salaries", salary)

    def start_project(self, name, difficulty=5):
        """Starts a new project."""
        self.project_manager.start_project(name, difficulty)

    def assign_employee(self, employee_name, project_name):
        """Assigns an employee to a project."""
        project = next((p for p in self.project_manager.projects if p.name == project_name), None)
        if project:
            self.employee_manager.assign_employee_to_project(employee_name, project)
        else:
            print(f"Project '{project_name}' not found.")

    def simulate_day(self, day_number):
        """Simulates a full in-game day, including legitimate and shady business activities."""
        print(f"\n📅 Day {day_number}: Debug: Starting Day Simulation...")

        # Employees work on projects
        for employee in self.employee_manager.employees:
            if employee.assigned_project:
                employee.work()

        # Collect user data from active apps
        total_users = random.randint(1000, 50000)
        self.user_data_sales.collect_data(total_users)

        # Rival Companies Take Action
        player_market_share = 25
        player_reputation = self.social_media.company_reputation
        self.rival_manager.check_rival_reactions(player_market_share, player_reputation)

        # Run shady dealings (random chance each day)
        if random.randint(1, 100) < 30:  # 30% chance of shady business activity
            shady_choice = random.choice(["sell_data", "nft_scam", "crypto_pump", "engagement_fraud"])
            if shady_choice == "sell_data":
                self.sell_user_data("black_market")
            elif shady_choice == "nft_scam":
                self.run_nft_scam("MoonApes", random.choice(["hype", "dump"]))
            elif shady_choice == "crypto_pump":
                self.run_crypto_scam("TechCoin", random.choice(["pump", "dump"]))
            elif shady_choice == "engagement_fraud":
                self.run_engagement_fraud("Fake Review Campaign", 5000)

        # Generate revenue from completed projects
        for project in self.project_manager.projects:
            if project.is_completed:
                revenue = project.difficulty * 5000
                self.economy.update_revenue(revenue)

        # Deduct salaries and expenses at the end of the day
        total_salaries = self.employee_manager.calculate_total_daily_salary()
        self.economy.update_expenses("Salaries", total_salaries)
        self.economy.apply_recurring_expenses(len(self.employee_manager.employees))

        # Conduct performance reviews every 5 days
        if day_number % 5 == 0:
            self.employee_manager.conduct_performance_reviews()

        # Social Media Post Generation every other day
        if day_number % 2 == 0:
            employee_state = {
                "happiness": sum(emp.happiness for emp in self.employee_manager.employees) / max(1, len(self.employee_manager.employees)),
                "enthusiasm": sum(emp.enthusiasm for emp in self.employee_manager.employees) / max(1, len(self.employee_manager.employees))
            }
            company_state = {"name": "TechnoloJesus"}
            self.social_media.generate_post(company_state, employee_state)

        # Roll for random events
        event_effect = self.random_events.roll_event({"name": "TechnoloJesus"})
        self.handle_random_event(event_effect)

        # Show financial summary
        self.economy.get_expense_report()

    def handle_random_event(self, event_effect):
        """Applies effects from random events."""
        print(f"Debug: Handling Event Effect - {event_effect}")

        if event_effect == "double_revenue":
            self.economy.update_revenue(self.economy.revenue)
        elif event_effect == "funding_boost":
            self.economy.update_revenue(10000)
        elif event_effect == "market_boost":
            print("📈 More customers are using your product!")
        elif event_effect == "productivity_boost":
            for emp in self.employee_manager.employees:
                emp.enthusiasm += 10
        elif event_effect == "market_crash":
            self.economy.update_revenue(-self.economy.revenue * 0.5)
        elif event_effect == "enthusiasm_drop":
            for emp in self.employee_manager.employees:
                emp.enthusiasm -= 20
        elif event_effect == "competitor_rivalry":
            print("🚨 A competitor launched a better product! Your market share drops.")
        elif event_effect == "reputation_loss":
            self.social_media.company_reputation -= 10
        elif event_effect == "nothing":
            print("Nothing significant happened today.")

    def sell_user_data(self, buyer):
        """Allows the player to sell stored user data."""
        self.user_data_sales.sell_data(buyer, self.economy, self.social_media)

    def run_nft_scam(self, collection_name, strategy):
        """Runs an NFT scam."""
        self.crypto_scams.manipulate_nft_market(collection_name, strategy)

    def run_crypto_scam(self, token_name, strategy):
        """Runs a crypto pump-and-dump scam."""
        self.crypto_scams.manipulate_crypto_market(token_name, strategy)

    def run_engagement_fraud(self, campaign_name, budget):
        """Runs engagement fraud for fake app reviews and rankings."""
        self.crypto_scams.run_engagement_fraud(campaign_name, budget)

if __name__ == "__main__":
    try:
        print("Debug: Starting TechnoloJesus Simulation...")
        simulation = StartupSimulation()

        # Setup initial employees and projects
        simulation.hire_employee("Alice", "Software Engineer")
        simulation.hire_employee("Bob", "Product Manager")

        simulation.start_project("AI Chatbot", difficulty=8)
        simulation.assign_employee("Alice", "AI Chatbot")

        # Run game loop
        for day in range(10):
            print(f"Debug: Running Day {day + 1}...")
            simulation.simulate_day(day + 1)

    except Exception as e:
        print(f"Error: {e}")
