import random

class ClickFarms:
    def __init__(self):
        """Handles Pakistani click farm mechanics."""
        self.click_farm_risk = 40  # 40% risk of being caught

    def hire_click_farm(self, app_name, budget):
        """Player hires a click farm to boost an app's popularity."""
        fake_downloads = budget * random.randint(100, 500)  # More money = more fake downloads
        detection_roll = random.randint(1, 100)

        print(f"📈 '{app_name}' received {fake_downloads} fake downloads from a click farm!")

        if detection_roll <= self.click_farm_risk:
            print(f"🚨 App Store detected manipulation! '{app_name}' is under review.")
            return "banned"
        else:
            print(f"✅ Click farm success! '{app_name}' is now trending.")
            return "success"
