"""
Mini Project 2: Employee Data Pipeline
Concepts: map(), filter(), reduce(), lambda functions, sorted()
"""

from functools import reduce

employees = [
    {"name": "Amit Sharma",   "dept": "Engineering", "salary": 75000},
    {"name": "Priya Singh",   "dept": "Marketing",   "salary": 52000},
    {"name": "Rahul Verma",   "dept": "Engineering", "salary": 90000},
    {"name": "Sneha Patel",   "dept": "HR",          "salary": 48000},
    {"name": "Karan Mehta",   "dept": "Engineering", "salary": 60000},
    {"name": "Nisha Gupta",   "dept": "Marketing",   "salary": 71000},
    {"name": "Vikram Bose",   "dept": "HR",          "salary": 55000},
    {"name": "Anjali Rao",    "dept": "Engineering", "salary": 83000},
]


# ── 1. map()
# Give every employee a 10% salary raise using map + lambda
raised_salaries = list(map( lambda emp: {**emp, "salary": int(emp["salary"] * 1.10)},employees))

print("=" * 55)
print("   After 10% Salary Raise (map + lambda)")
print("=" * 55)
for emp in raised_salaries:
    print(f"  {emp['name']:<20} ₹{emp['salary']:>8,}")


# ── 2. filter() Keep only high earners (salary > 60,000) after the raise
high_earners = list(filter(
    lambda emp: emp["salary"] > 60000,
    raised_salaries
))

print(f"\n{'=' * 55}")
print("   High Earners (salary > ₹60,000) (filter + lambda)")
print("=" * 55)
for emp in high_earners:
    print(f"  {emp['name']:<20} ₹{emp['salary']:>8,}  [{emp['dept']}]")


# ── 3. reduce()────
# Calculate total salary bill of high earners
total_salary = reduce(
    lambda acc, emp: acc + emp["salary"],
    high_earners,
    0
)

print(f"\n   Total salary bill (reduce + lambda) : ₹{total_salary:,}\n")


# ── 4. sorted() with lambda key──
# Sort all employees by salary (highest first)
top_employees = sorted(
    employees,
    key=lambda emp: emp["salary"],
    reverse=True
)

print("=" * 55)
print("   All Employees Ranked by Salary (sorted + lambda)")
print("=" * 55)
for rank, emp in enumerate(top_employees, start=1):
    print(f"  {rank}. {emp['name']:<20} ₹{emp['salary']:>8,}  [{emp['dept']}]")


# ── 5. Chained pipeline────
# Find average salary of Engineering dept employees after raise
eng_avg = reduce(
    lambda acc, emp: acc + emp["salary"],
    filter(lambda emp: emp["dept"] == "Engineering", raised_salaries),
    0
) / len(list(filter(lambda emp: emp["dept"] == "Engineering", raised_salaries)))

print(f"\n    Avg Engineering salary after raise : ₹{eng_avg:,.0f}")
print()
