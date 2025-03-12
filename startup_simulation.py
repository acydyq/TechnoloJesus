import random
from game_logic.employees import EmployeeManager
from game_logic.projects import ProjectManager
from game_logic.economy import Economy
from game_logic.social_media import SocialMedia
from game_logic.random_events import RandomEvents
from game_logic.rival_companies import RivalManager
from game_logic.user_data_sales import UserDataSales
from game_logic.crypto_scams import CryptoScams
from game_logic.investor_relations import InvestorRelations

class StartupSimulation:
    def __init__(self):
        """Initializes all core systems, including competitive rivalries and investor relations."""
        print("Debug: Initializing StartupSimulation...")
        self.economy = Economy()
        self.employee_manager = EmployeeManager()
        self.project_manager = ProjectManager()
        self.social_media = SocialMedia()
        self.random_events = RandomEvents()
        self.rival_manager = RivalManager()
        self.user_data_sales = UserDataSales()
        self.crypto_scams = CryptoScams()
        self.investor_relations = InvestorRelations()

    def hire_employee(self, name, role):
        """Hires an employee and deducts salary costs."""
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
        """Simulates a full in-game day, including investor relations and competitive rivalries."""
        print(f"\n📅 Day {day_number}: Debug: Starting Day Simulation...")

        # Employees work on projects
        for employee in self.employee_manager.employees:
            if employee.assigned_project:
                employee.work()

        # Rival Companies Take Action
        player_market_share = 25
        player_reputation = self.social_media.company_reputation
        player_funds = self.economy.funds
        action, value = self.rival_manager.check_rival_reactions(player_market_share, player_funds, player_reputation)

        if action == "lawsuit":
            self.economy.update_expenses("Legal Fees", value)
        elif action == "market_attack":
            print("📉 Your revenue drops due to market competition.")
        elif action == "sabotage":
            print("💀 A key employee mysteriously quits!")
        elif action == "hostile_takeover":
            print("🚨 You must raise funds or negotiate to prevent losing your company!")

        # Evaluate investor satisfaction
        self.investor_relations.evaluate_investors(self.economy.revenue)

        # Deduct salaries and expenses at the end of the day
        total_salaries = self.employee_manager.calculate_total_daily_salary()
        self.economy.update_expenses("Salaries", total_salaries)
        self.economy.apply_recurring_expenses(len(self.employee_manager.employees))

        # Show financial summary
        self.economy.get_expense_report()

        # **Wait for Player Confirmation Before Advancing to the Next Day**
        self.prompt_end_of_day()

    def prompt_end_of_day(self):
        """Asks the player if they want to end the day or manage business before continuing."""
        while True:
            print("\n🕛 End of Day Menu:")
            print("1. End the day and continue to the next.")
            print("2. Hire/Firing Employees")
            print("3. Seek Investment")
            print("4. Check Financial Reports")
            print("5. View Rival Market Position")
            print("6. Exit Game")
            
            choice = input("Choose an option: ")

            if choice == "1":
                print("✅ Proceeding to the next day...")
                break
            elif choice == "2":
                name = input("Enter employee name to hire/fire: ")
                role = input("Enter role (or leave blank to fire): ")
                if role:
                    self.hire_employee(name, role)
                else:
                    self.employee_manager.fire_employee(name)
            elif choice == "3":
                self.pitch_investors()
            elif choice == "4":
                self.economy.get_expense_report()
            elif choice == "5":
                for rival in self.rival_manager.rivals:
                    print(rival)
            elif choice == "6":
                print("👋 Exiting game...")
                exit()
            else:
                print("❌ Invalid choice. Try again.")

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

    def pitch_investors(self):
        """Allows the player to pitch to investors for funding."""
        self.investor_relations.pitch_investors(self.economy)

if __name__ == "__main__":
    try:
        print("Debug: Starting TechnoloJesus Simulation...")
        simulation = StartupSimulation()

        # Setup initial employees and projects
        simulation.hire_employee("Alice", "Software Engineer")
        simulation.hire_employee("Bob", "Product Manager")

        simulation.start_project("AI Chatbot", difficulty=8)
        simulation.assign_employee("Alice", "AI Chatbot")

        # Player can pitch investors
        simulation.pitch_investors()

        # **Run Game Loop with Player-Controlled End-of-Day Progression**
        day = 1
        while True:
            print(f"Debug: Running Day {day}...")
            simulation.simulate_day(day)
            day += 1

    except Exception as e:
        print(f"Error: {e}")
