import random

class CryptoScams:
    def __init__(self):
        """Handles NFT scams, crypto pump-and-dump, and engagement fraud."""
        self.nft_collections = []
        self.cryptos = []
        self.engagement_farms = []

    def create_nft_scam(self, collection_name):
        """Creates a fake NFT collection."""
        base_price = random.randint(500, 5000)
        self.nft_collections.append({
            "name": collection_name,
            "price": base_price,
            "hype": 50,
            "risk": random.randint(10, 60),
        })
        print(f"🎨 Created NFT scam: {collection_name}. Starting price: ${base_price}.")

    def manipulate_nft_market(self, collection_name, strategy):
        """Player manipulates an NFT collection."""
        nft = next((n for n in self.nft_collections if n["name"] == collection_name), None)
        if not nft:
            print("❌ NFT collection not found.")
            return

        if strategy == "hype":
            nft["hype"] += random.randint(10, 30)
            nft["price"] += random.randint(100, 1000)
            print(f"🚀 Hyped {collection_name}. New price: ${nft['price']}.")

        elif strategy == "dump":
            print(f"💰 Dumped {collection_name} for ${nft['price']}.")
            self.nft_collections.remove(nft)

            # Risk Check
            roll = random.randint(1, 100)
            if roll <= nft["risk"]:
                print("🚨 SCAM EXPOSED! Authorities are investigating.")
                return "banned"
            else:
                print("✅ Got away with the NFT dump.")
                return "success"

    def create_crypto_scam(self, token_name):
        """Creates a fake cryptocurrency and pumps its value."""
        base_value = round(random.uniform(0.001, 1.0), 4)
        self.cryptos.append({
            "name": token_name,
            "value": base_value,
            "hype": 50,
            "risk": random.randint(20, 80),
        })
        print(f"💰 Created crypto scam: {token_name}. Starting value: ${base_value}.")

    def manipulate_crypto_market(self, token_name, strategy):
        """Player manipulates a fake crypto token."""
        crypto = next((c for c in self.cryptos if c["name"] == token_name), None)
        if not crypto:
            print("❌ Cryptocurrency not found.")
            return

        if strategy == "pump":
            crypto["hype"] += random.randint(15, 40)
            crypto["value"] *= random.uniform(1.5, 3.0)
            print(f"📈 Pumped {token_name}. New value: ${crypto['value']:.4f}")

        elif strategy == "dump":
            print(f"💰 Dumped {token_name} tokens. Cashed out at ${crypto['value']:.4f}.")
            self.cryptos.remove(crypto)

            # Risk Check
            roll = random.randint(1, 100)
            if roll <= crypto["risk"]:
                print("🚨 SEC INVESTIGATION! Authorities are after you!")
                return "banned"
            else:
                print("✅ Got away with the crypto dump.")
                return "success"

    def run_engagement_fraud(self, campaign_name, budget):
        """Runs fake engagement farming for boosting app rankings."""
        fake_reviews = budget * random.randint(50, 300)
        detection_roll = random.randint(1, 100)

        print(f"📊 '{campaign_name}' received {fake_reviews} fake positive reviews!")

        if detection_roll <= 30:  # 30% chance of getting caught
            print(f"🚨 Fake reviews detected! '{campaign_name}' is under review.")
            return "banned"
        else:
            print(f"✅ Engagement fraud successful for '{campaign_name}'.")
            return "success"
