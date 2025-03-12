import random

class KnockoffApps:
    def __init__(self):
        """Handles Chinese knockoff app mechanics."""
        self.knockoff_risk = 30  # Default 30% risk of a knockoff appearing
        self.active_knockoffs = {}

    def check_for_knockoff(self, original_app):
        """Determines if a knockoff version of the player's app will be created."""
        roll = random.randint(1, 100)
        if roll <= self.knockoff_risk:
            knockoff_name = f"{original_app['name']} Pro Max"
            self.active_knockoffs[knockoff_name] = {
                "original": original_app["name"],
                "stealing_users": random.uniform(0.1, 0.5),  # 10-50% market share loss
                "legal_action_cost": random.randint(5000, 20000),
            }
            print(f"🚨 A Chinese knockoff of '{original_app['name']}' has appeared: '{knockoff_name}'!")

    def handle_knockoff(self, knockoff_name, strategy):
        """Player decides how to handle a knockoff app."""
        knockoff = self.active_knockoffs.get(knockoff_name)
        if not knockoff:
            print("No such knockoff exists.")
            return

        if strategy == "innovate":
            success_chance = random.randint(1, 100)
            if success_chance > 50:
                print(f"💡 You out-innovated '{knockoff_name}'. Market share recovered!")
                del self.active_knockoffs[knockoff_name]
            else:
                print(f"❌ Innovation failed. '{knockoff_name}' still dominates.")

        elif strategy == "sue":
            print(f"⚖️ You sued '{knockoff_name}'. It cost ${knockoff['legal_action_cost']}.")
            del self.active_knockoffs[knockoff_name]

        elif strategy == "clone":
            print(f"🔄 You reverse-engineered '{knockoff_name}' and released your own version.")
            del self.active_knockoffs[knockoff_name]

    def get_active_knockoffs(self):
        """Returns a list of active knockoffs."""
        return self.active_knockoffs
