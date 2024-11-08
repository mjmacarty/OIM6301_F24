balance = 1000
INTEREST = .01
YEARS = 5
MONTHS = 12
year = 1


for month in range(1, MONTHS * YEARS + 1):
    if month % 12 == 1:
        print()
        print(f" Year {year} ".center(50, "="))
        print(f"{'Month':<15}{'Return':^15}{'Ending Balance':>20}")
        print()
        year += 1
    interest = balance * INTEREST
    balance += interest
    print(f"{month:<15}{interest:^15.2f}{balance:>20,.2f}")
