import random

class SocialMedia:
    def __init__(self):
        """Tracks social media sentiment and posts about the company."""
        self.company_reputation = 50  # Starts at a neutral 50/100
        self.posts = []

    def generate_post(self, company_state, employee_state):
        """Creates a randomized social media post based on company performance."""
        roll = random.randint(1, 100)

        # Determine post type based on company and employee conditions
        if roll <= 30 and employee_state["happiness"] < 50:
            post_type = "Negative"
        elif 30 < roll <= 70:
            post_type = "Neutral"
        else:
            post_type = "Positive"

        # Sample posts
        post_templates = {
            "Positive": [
                f"Wow! Just got a raise at {company_state['name']}! Loving the startup life. 🚀💰",
                f"{company_state['name']} is killing it! Another great product launch. 🔥",
                f"The office vibe at {company_state['name']} is next level. Free snacks, great perks, amazing team!"
            ],
            "Neutral": [
                f"Another day, another code review. Startup grind at {company_state['name']} continues. 🤷",
                f"Hanging in there at {company_state['name']}. Work’s alright, hoping for some bonuses soon. 💼",
                f"Office coffee machine is broken again. Why do I even work here? ☕😑"
            ],
            "Negative": [
                f"Ugh, another 12-hour shift at {company_state['name']}. Burnout is real. 😩",
                f"{company_state['name']} is cutting costs again. No bonuses this month. Morale is low. 😒",
                f"Might start looking for a new job... {company_state['name']} ain't what it used to be. 🚶‍♂️"
            ],
        }

        post_content = random.choice(post_templates[post_type])
        self.posts.append({"type": post_type, "content": post_content})

        # Adjust company reputation
        if post_type == "Positive":
            self.company_reputation += random.randint(2, 5)
        elif post_type == "Negative":
            self.company_reputation -= random.randint(3, 7)

        # Limit reputation to 0-100
        self.company_reputation = max(0, min(100, self.company_reputation))

        print(f"📢 Social Media Update: {post_content} (Reputation: {self.company_reputation}/100)")

    def get_latest_posts(self):
        """Returns the latest social media posts."""
        return self.posts[-5:]  # Show last 5 posts
