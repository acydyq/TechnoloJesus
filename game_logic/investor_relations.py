import random

class Investor:
    def __init__(self, name, investment_amount, control_demand, expectation):
        """Represents an investor offering funding."""
        self.name = name
        self.investment_amount = investment_amount
        self.control_demand = control_demand  # % equity they want
        self.expectation = expectation  # Required profit growth

    def evaluate_offer(self, player_revenue):
        """Determines if the player meets investor expectations."""
        if player_revenue >= self.expectation:
            print(f"✅ Investor {self.name} is satisfied with your performance.")
            return True
        else:
            print(f"⚠️ Investor {self.name} is disappointed! They may withdraw funding.")
            return False

    def __repr__(self):
        return f"{self.name} - Investment: ${self.investment_amount} | Control Demand: {self.control_demand}% | Target Revenue: ${self.expectation}"

class InvestorRelations:
    def __init__(self):
        """Manages investor funding and relations."""
        self.investors = [
            Investor("Angel Fund", 50000, 5, 20000),
            Investor("VentureTech Capital", 200000, 20, 80000),
            Investor("MegaCorp Buyout", 500000, 50, 200000)
        ]
        self.active_investors = []

    def pitch_investors(self, economy):
        """Allows the player to pitch investors for funding."""
        print("\n📊 Available Investors:")
        for i, investor in enumerate(self.investors):
            print(f"{i+1}. {investor}")

        choice = int(input("Choose an investor (1-3) or 0 to cancel: "))
        if choice == 0:
            print("🚫 Pitch canceled.")
            return

        selected_investor = self.investors[choice - 1]
        self.active_investors.append(selected_investor)
        economy.update_revenue(selected_investor.investment_amount)
        print(f"💰 {selected_investor.name} invested ${selected_investor.investment_amount} for {selected_investor.control_demand}% control.")

    def evaluate_investors(self, player_revenue):
        """Checks if the player is meeting investor expectations."""
        for investor in self.active_investors:
            if not investor.evaluate_offer(player_revenue):
                print(f"❌ {investor.name} is pulling out funding! You lose their investment.")
                self.active_investors.remove(investor)
