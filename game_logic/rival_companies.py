import random

class RivalCompany:
    def __init__(self, name, strength, aggression, market_share):
        """Initializes a rival company with its attributes."""
        self.name = name
        self.strength = strength  # Determines business success
        self.aggression = aggression  # Determines how hostile they are
        self.market_share = market_share  # Percentage of the industry they control

    def take_action(self, player_reputation):
        """Determines what the rival company will do based on its aggression and player's reputation."""
        roll = random.randint(1, 100)

        if roll < self.aggression and player_reputation > 60:
            return "lawsuit" if roll % 2 == 0 else "sabotage"
        elif roll < self.aggression + 20:
            return "market_share_attack"
        else:
            return "nothing"

    def react_to_player(self, player_success):
        """Rival companies react to the player's market success."""
        if player_success > self.market_share * 1.2:  # If the player is growing too fast
            print(f"⚠️ Rival company {self.name} is taking action against you!")
            return self.take_action(player_success)
        return "nothing"

    def __repr__(self):
        return f"{self.name} - Strength: {self.strength} | Aggression: {self.aggression} | Market Share: {self.market_share}%"

class RivalManager:
    def __init__(self):
        """Manages all rival companies in the industry."""
        self.rivals = [
            RivalCompany("CodeKiller Ltd.", strength=85, aggression=70, market_share=20),
            RivalCompany("ShadowSoft", strength=92, aggression=60, market_share=25),
            RivalCompany("ByteRiot", strength=78, aggression=80, market_share=18),
        ]

    def check_rival_reactions(self, player_market_share, player_reputation):
        """Checks how rivals respond to player's success."""
        for rival in self.rivals:
            action = rival.react_to_player(player_market_share)
            if action == "lawsuit":
                print(f"⚖️ {rival.name} has filed a lawsuit against you!")
            elif action == "sabotage":
                print(f"💀 {rival.name} has sabotaged your project!")
            elif action == "market_share_attack":
                print(f"📉 {rival.name} is aggressively taking your users!")

    def get_rivals(self):
        """Returns a list of active rivals."""
        return self.rivals
