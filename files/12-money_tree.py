# money tree calculator
starting_balance = 1000
balance = starting_balance
rate = 0.02
withdrawal = 250
goal = 1e6
month = 0

print(f"{'Month':<15}{'Balance':>10}")
print("-" * 25)

while balance < goal:
    month += 1
    balance  *= (1 + rate)
    if month % 12 == 0:
        balance -= withdrawal
        print()
        print(f"{'Month':<15}{'Balance':>10}")
        print("-" * 25)
    print(f"{month:<15}{balance:10,.2f}")

years = month / 12
CAGR = (balance / starting_balance) ** (1/years) - 1

print("-" * 25)
print(f"It took {years:.1f} years")
print(f"you earned: {CAGR:.2%}")