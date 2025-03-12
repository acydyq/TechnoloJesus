import random

class UserDataSales:
    def __init__(self):
        """Manages the selling of user data as an optional revenue stream."""
        self.data_collected = 0  # Tracks the amount of data available for sale
        self.sell_risk = {
            "advertisers": {"chance": 5, "reward": (500, 1500), "fine": 5000},
            "political_groups": {"chance": 20, "reward": (2000, 6000), "fine": 20000},
            "black_market": {"chance": 50, "reward": (10000, 50000), "fine": 100000},
        }

    def collect_data(self, users):
        """Collects user data over time based on app users."""
        collected = users * random.uniform(0.01, 0.05)  # 1-5% of users' data collected
        self.data_collected += int(collected)
        print(f"📊 Collected data on {int(collected)} users. Total stored: {self.data_collected}.")

    def sell_data(self, buyer, economy, social_media):
        """Sells collected user data to a chosen buyer."""
        if self.data_collected == 0:
            print("❌ No user data available to sell.")
            return

        if buyer not in self.sell_risk:
            print("❌ Invalid buyer type.")
            return

        risk = self.sell_risk[buyer]
        roll = random.randint(1, 100)
        revenue = random.randint(*risk["reward"])
        
        # Process Sale
        print(f"💰 Sold user data to {buyer}. Earned ${revenue}.")
        economy.update_revenue(revenue)
        self.data_collected = 0  # Reset stored data after sale

        # Risk Check
        if roll <= risk["chance"]:
            fine = risk["fine"]
            print(f"🚨 CAUGHT! Government fine of ${fine}. Reputation hit!")
            economy.update_expenses("Government Fines", fine)
            social_media.company_reputation -= random.randint(10, 30)
        else:
            print(f"✅ Data sale completed without issue.")

