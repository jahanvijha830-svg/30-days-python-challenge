def get_category_totals(expenses):
    category_totals = {}
    for exp in expenses:
        cat = exp["category"].title()
        amt = exp["amount"]
        category_totals[cat] = category_totals.get(cat, 0) + amt
    return category_totals

def print_ranked_report(category_totals):
    sorted_items = sorted(category_totals.items(), key=lambda x: x[1],reverse=True)
    total_spent = sum(category_totals.values())

    for rank, (category, amount) in enumerate(sorted_items, start=1):
        percent = (amount / total_spent) * 100
        print(f"{rank}. {category}: {amount} ({percent:.1f}%)")

expenses = [
    {"amount":2000, "category":"Maths","date":"17-08-2026"},
    {"amount":3000,"category":"Physics","date":"18-08-2026"},
    {"amount":1000,"category":"Chemistry","date":"19-08-2026"},
    {"amount":10000,"category":"Computer Science","date":"20-08-2026"},
    ]
totals = get_category_totals(expenses)
print_ranked_report(totals)

