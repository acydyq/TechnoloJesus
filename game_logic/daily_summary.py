class DailySummary:
    def __init__(self):
        """Stores daily reports."""
        self.reports = []

    def generate_summary(self, day, revenue, expenses, events):
        """Creates a daily summary report."""
        summary = {
            "Day": day,
            "Revenue": revenue,
            "Expenses": expenses,
            "Net Profit": revenue - expenses,
            "Events": events
        }
        self.reports.append(summary)

    def get_latest_summary(self):
        """Returns the latest report."""
        return self.reports[-1] if self.reports else None

    def print_summary(self, day):
        """Displays a daily report."""
        report = next((r for r in self.reports if r["Day"] == day), None)
        if report:
            print(f"\n📊 Daily Summary - Day {report['Day']}:")
            print(f"💰 Revenue: ${report['Revenue']}")
            print(f"📉 Expenses: ${report['Expenses']}")
            print(f"📈 Net Profit: ${report['Net Profit']}")
            print("📌 Events:", report["Events"])
        else:
            print(f"No report found for Day {day}.")
