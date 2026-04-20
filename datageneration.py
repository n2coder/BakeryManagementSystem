import pandas as pd
import random
from datetime import datetime, timedelta

# Items and prices
items = {
    "Cake": 25.00,
    "Pastry": 4.50,
    "Chocolate": 3.00,
    "Sandwich": 8.50,
    "Muffin": 3.50
}

# Date range
start_date = datetime(2026, 4, 1)
end_date = datetime(2026, 6, 30)

date_range = (end_date - start_date).days

data = []

for _ in range(2000):
    item = random.choice(list(items.keys()))
    price = items[item]
    
    random_days = random.randint(0, date_range)
    sale_date = start_date + timedelta(days=random_days)

    data.append([item, price, sale_date.strftime("%Y-%m-%d")])

# Create DataFrame
df = pd.DataFrame(data, columns=["item_name", "item_price", "sale_date"])

# Save to CSV
df.to_csv("bakery_sales_2000.csv", index=False)

print(df.head())
print("✅ 2000 rows dataset created!")