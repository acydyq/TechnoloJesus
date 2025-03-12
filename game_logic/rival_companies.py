import random

class RivalCompany:
    def __init__(self, name, strength, aggression, market_share, legal_budget):
        """Initializes a rival company with attributes."""
        self.name = name
        self.strength = strength
        self.aggression = aggression
        self.market_share = market_share
        self.legal_budget = legal_budget

    def take_action(self, player_market_share, player_funds, player_reputation):
        """Determines what the rival company will do based on the player's market position."""
        roll = random.randint(1, 100)

        if roll < self.aggression and player_market_share > self.market_share:
            return "lawsuit" if roll % 2 == 0 else "sabotage"
        elif roll < self.aggression + 20:
            return "market_attack"
        elif player_funds < 10000 and roll < self.aggression + 40:
            return "hostile_takeover"
        else:
            return "nothing"

    def react_to_player(self, player_market_share, player_funds, player_reputation):
        """Rival companies react to the player's market success or financial instability."""
        action = self.take_action(player_market_share, player_funds, player_reputation)
        if action == "lawsuit":
            print(f"⚖️ {self.name} has filed a lawsuit against you!")
        elif action == "sabotage":
            print(f"💀 {self.name} has sabotaged your projects!")
        elif action == "market_attack":
            print(f"📉 {self.name} launched a superior product and stole your customers!")
        elif action == "hostile_takeover":
            print(f"🚨 {self.name} is attempting a hostile takeover of your company!")
        return action

class RivalManager:
    def __init__(self):
        """Manages all rival companies in the industry."""
        self.rivals = [
            RivalCompany("CodeKiller Ltd.", strength=85, aggression=70, market_share=20, legal_budget=50000),
            RivalCompany("ShadowSoft", strength=92, aggression=60, market_share=25, legal_budget=70000),
            RivalCompany("ByteRiot", strength=78, aggression=80, market_share=18, legal_budget=60000),
        ]

    def check_rival_reactions(self, player_market_share, player_funds, player_reputation):
        """Checks how rivals respond to player's success or financial instability."""
        for rival in self.rivals:
            action = rival.react_to_player(player_market_share, player_funds, player_reputation)
            if action == "lawsuit":
                fine = random.randint(5000, 30000)
                return ("lawsuit", fine)
            elif action == "market_attack":
                return ("market_attack", -10)
            elif action == "sabotage":
                return ("sabotage", 0)
            elif action == "hostile_takeover":
                return ("hostile_takeover", 0)
        return ("nothing", 0)
