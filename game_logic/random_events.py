import random

class RandomEvents:
    def __init__(self):
        """Handles random game events triggered by a 1d100 dice roll."""
        self.events = {
            "Positive": [
                {"event": "Your app goes viral! Revenue doubles today!", "effect": "double_revenue"},
                {"event": "Unexpected angel investor! You gain $10,000 in funding.", "effect": "funding_boost"},
                {"event": "Competitor collapses! You gain 5% more customers.", "effect": "market_boost"},
                {"event": "Employee productivity spikes due to inspiration! Work efficiency +20%.", "effect": "productivity_boost"},
            ],
            "Negative": [
                {"event": "Market crash! Revenue drops by 50% today.", "effect": "market_crash"},
                {"event": "Major employee burnout. Enthusiasm drops sharply.", "effect": "enthusiasm_drop"},
                {"event": "Competitor launches a superior version of your app. Market share -10%.", "effect": "competitor_rivalry"},
                {"event": "Employee scandal! PR disaster reduces company reputation by 10.", "effect": "reputation_loss"},
            ],
            "Neutral": [
                {"event": "Routine day. Nothing special happens.", "effect": "nothing"},
                {"event": "Mild system bug discovered. Slight delay in development.", "effect": "minor_bug"},
                {"event": "Startup networking event attended. Potential investor interest.", "effect": "networking_opportunity"},
            ],
        }

    def roll_event(self, company_state):
        """Rolls a 1d100 and determines if a random event occurs."""
        roll = random.randint(1, 100)

        if roll <= 15:
            event_type = "Negative"
        elif 15 < roll <= 70:
            event_type = "Neutral"
        else:
            event_type = "Positive"

        event = random.choice(self.events[event_type])
        print(f"\n🎲 Random Event Triggered: {event['event']}")

        return event["effect"]
