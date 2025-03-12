class Economy:
    def __init__(self, starting_funds=50000):
        """Initializes company finances with realistic expenses and salaries."""
        self.funds = starting_funds
        self.revenue = 0
        self.expenses = 0
        self.expense_breakdown = {
            "Salaries": 0,  # Employee salaries are dynamically updated
            "Rent": 100,  # Daily rent cost
            "Utilities": 13,  # Daily electricity + internet + water
            "Food & Groceries": 0,  # Calculated per employee
            "Office Supplies": 17,  # Software, desks, snacks
            "Recreational Expenses": 33,  # Gym, weed, team outings
        }

    def update_revenue(self, amount):
        """Increases revenue when the company earns money."""
        self.revenue += amount
        self.funds += amount
        print(f"Earned ${amount}. Total funds: ${self.funds}")

    def update_expenses(self, category, amount):
        """Tracks and deducts expenses for specific categories."""
        if category in self.expense_breakdown:
            self.expense_breakdown[category] += amount
        self.expenses += amount
        self.funds -= amount
        print(f"Spent ${amount} on {category}. Remaining funds: ${self.funds}")

    def calculate_total_daily_expenses(self, employee_count):
        """Calculates total expenses for the day, factoring in the number of employees."""
        total = sum(self.expense_breakdown.values())
        food_cost = 20 * employee_count  # Food cost per employee per day
        total += food_cost
        return total

    def apply_recurring_expenses(self, employee_count):
        """Deducts all fixed daily expenses including dynamic food costs."""
        total_expense = self.calculate_total_daily_expenses(employee_count)
        self.expenses += total_expense
        self.funds -= total_expense
        print(f"\nTotal Daily Expenses Deducted: ${total_expense}")
        print(f"Remaining Funds After Expenses: ${self.funds}\n")

    def calculate_profit(self):
        """Returns net profit/loss."""
        return self.revenue - self.expenses

    def can_afford(self, amount):
        """Checks if the company has enough funds for an expense."""
        return self.funds >= amount

    def get_expense_report(self):
        """Displays a detailed breakdown of expenses."""
        print("\nExpense Breakdown:")
        for category, amount in self.expense_breakdown.items():
            print(f"{category}: ${amount}")
        print(f"Total Expenses: ${self.expenses}\n")

# Test economy system with updated expenses
if __name__ == "__main__":
    economy = Economy()
    economy.update_revenue(10000)
    economy.apply_recurring_expenses(3)  # Example: 3 employees
    economy.get_expense_report()
    print("Net Profit:", economy.calculate_profit())
