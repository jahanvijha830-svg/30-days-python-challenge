import json
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

def is_valid_expense(exp):
    if not isinstance(exp.get("amount"),(int,float)):
        return False
    if exp["amount"] <= 0:
        return False
    if not isinstance(exp.get("category"),str) or exp["category"].strip() == "":
        return False
    return True

def get_valid_expenses(expenses):
    valid= []
    invalid_count = 0
    for exp in expenses:
        if is_valid_expense(exp):
            valid.append(exp)
        else:
            invalid_count += 1
    print(f"There are {invalid_count} invalid expenses.")
    return valid

expenses = [
    {"amount":2000, "category":"Maths","date":"17-08-2026"},
    {"amount":3000,"category":"Physics","date":"18-08-2026"},
    {"amount":1000,"category":"Chemistry","date":"19-08-2026"},
    {"amount":10000,"category":"Computer Science","date":"20-08-2026"},
    {"amount":"abc","category":"books","date":"21-08-22026"}
]
def save_expenses(expenses,filename="expenses.json"):
    with open(filename,"w") as f:
        json.dump(expenses,f,indent=4)
def load_expenses(filename="expenses.json"):
    try:
        with open(filename,"r") as f:
            return json.load(f)
    except FileNotFoundError:
        return[]




clean_expenses = get_valid_expenses(expenses)
totals = get_category_totals(clean_expenses)
print_ranked_report(totals)

# ----Day-12: save and reload ----
save_expenses(clean_expenses)
print("saved to expenses.json")

reloaded = load_expenses()
print("Reloaded from file:",reloaded)

# confirm the pipeline still works on the reloaded data
totals_from_file = get_category_totals(reloaded)
print_ranked_report(totals_from_file)
