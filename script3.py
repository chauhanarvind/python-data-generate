import csv
import random
from datetime import datetime, timedelta

# Config
categories = {
    "Rent": (-1500, -800),
    "Food": (-200, -20),
    "Salary": (10000, 20000),
    "Transport": (-100, -10),
    "EMI": (-999, -400),
    "Social": (-800, -100),
    "Miscl": (-150, -10),
    "Other": (-300, 300),  # could be debit or credit
}

descriptions = {
    "Rent": ["Monthly Rent", "Flat rent", "Apartment rent"],
    "Food": ["Lunch", "Dinner", "Snacks", "Groceries", "Pizza", "Brunch"],
    "Salary": ["Company salary", "Freelance payout"],
    "Transport": ["Bus card", "Metro", "Uber"],
    "EMI": ["Phone EMI", "Laptop EMI", "Loan Payment"],
    "Social": ["Party", "Dinner out", "Movies", "School friends"],
    "Miscl": ["Stationery", "Top-up", "Donation"],
    "Other": ["Transfer from friend", "To family", "Misc adjustment"],
}

start_date = datetime.today() - timedelta(days=180)
transactions = []

for _ in range(1000):  # ~5000 transactions
    days_offset = random.randint(0, 365)
    tx_date = (start_date + timedelta(days=days_offset)).strftime("%d-%m-%Y")
    category = random.choice(list(categories.keys()))
    min_amt, max_amt = categories[category]
    amount = round(random.uniform(min_amt, max_amt), 2)
    description = random.choice(descriptions[category])
    account = "CUB - online payment"

    transactions.append([tx_date, account, category, description, amount])

# Write to CSV
with open("transactions.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["date", "account", "Category", "description", "amount"])
    writer.writerows(transactions)

print("✅ transactions.csv generated with", len(transactions), "rows.")
