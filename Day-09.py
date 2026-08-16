expense = {"amount":100,
           "category":"Books",
           "date":"15-08-2020"}


expenses = [
    {"amount":200,"category":"Maths","date":"15-08-2026"},
    {"amount":500,"category":"Physics","date":"16-08-2020"},
    {"amount":100,"category":"Chemistry","date":"17-08-2020"},
]
category_totals = {"Maths": 200, "Physics": 500, "Chemistry": 100}
sorted_items = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)
print(sorted_items)


for rank, (category, amount) in enumerate(sorted_items, start=1):
    print(f"{rank}. {category}: {amount}")

total_spent = sum(category_totals.values())
for category, amount in sorted_items:
    percent = (amount / total_spent)*100
    print(f"{category}: {amount} ({percent:.1f}%)")


