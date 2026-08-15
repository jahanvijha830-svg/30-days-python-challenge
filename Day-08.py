expense = {"amount":100,
           "category":"Books",
           "date":"15-08-2020"}
from datetime import date

today = date.today()
print(today)
print(today.strftime("%d-%m-%Y"))

current_month = date.today().strftime("%m")
print(current_month)

expenses = [
    {"amount":200,"category":"Maths","date":"15-08-2026"},
    {"amount":500,"category":"Physics","date":"16-08-2020"},
    {"amount":100,"category":"Chemistry","date":"17-08-2020"},
]
category_totals ={}

for exp in expenses:
    cat = exp["category"].title()
    amt = exp["amount"]
    exp_date = exp["date"]
    category_totals[cat] = category_totals.get(cat,0) + amt

print(category_totals)

total_spent = sum(category_totals.values())
top_category = max(category_totals,key=category_totals.get)
print(f"The top category is: {top_category}")
print(f"The total spent is: {total_spent}")
