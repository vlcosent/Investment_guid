#!/usr/bin/env python3
"""
CORRECTED CALCULATIONS with verified CPI data
Using Sep 2025 CPI = 324.368 (most recent available)
"""

import math

# VERIFIED CPI DATA
CPI = {
    'Nov 1995': 153.6,
    'Nov 2005': 197.6,
    'Nov 2015': 237.336,
    'Nov 2020': 260.229,
    'Sep 2025': 324.368,  # Most recent available
}

# QQQ Prices - need to verify these too
QQQ_PRICES = {
    'Nov 2005': 39.50,  # Need to verify
    'Nov 2015': 112.00,  # Need to verify
    'Nov 2020': 289.00,  # Need to verify
    'Nov 2025': 610.00,  # Current - need to verify
}

print("="*80)
print("CORRECTED INFLATION CALCULATIONS")
print("="*80)

current_cpi = CPI['Sep 2025']

# Calculate for each period
periods = [
    (5, 'Nov 2020', CPI['Nov 2020'], 4.83),  # Nov 2020 to Sep 2025 = 4.83 years
    (10, 'Nov 2015', CPI['Nov 2015'], 9.83),  # Nov 2015 to Sep 2025 = 9.83 years
    (20, 'Nov 2005', CPI['Nov 2005'], 19.83),  # Nov 2005 to Sep 2025 = 19.83 years
    (30, 'Nov 1995', CPI['Nov 1995'], 29.83),  # Nov 1995 to Sep 2025 = 29.83 years
]

for label, date, old_cpi, actual_years in periods:
    multiplier = current_cpi / old_cpi
    cumulative = (multiplier - 1) * 100
    annual = (pow(multiplier, 1/actual_years) - 1) * 100

    print(f"\n{label} YEARS AGO ({date} to Sep 2025):")
    print(f"  Price Multiplier: {multiplier:.6f}")
    print(f"  Cumulative Inflation: {cumulative:.2f}%")
    print(f"  Annual Avg Rate: {annual:.2f}%")
    print(f"  $10,000 then = ${10000/multiplier:.2f} today")
    print(f"  $10,000 today needs ${10000*multiplier:.2f} then")

print("\n" + "="*80)
print("PURCHASING POWER OF SAVINGS - CORRECTED")
print("="*80)

savings = [5000, 10000, 25000, 50000]

for label, date, old_cpi, _ in periods:
    multiplier = current_cpi / old_cpi
    print(f"\n{label} YEARS AGO ({date}):")
    for amount in savings:
        value_today = amount / multiplier
        loss = amount - value_today
        print(f"  ${amount:,} -> ${value_today:,.2f} (Loss: ${loss:,.2f})")

print("\n" + "="*80)
print("SALARY ADJUSTMENTS - CORRECTED")
print("="*80)

salaries = [50000, 65000, 80000, 100000]

for label, date, old_cpi, _ in periods:
    multiplier = current_cpi / old_cpi
    print(f"\n{label} YEARS AGO ({date}):")
    for salary in salaries:
        if_no_raise = salary / multiplier
        needed = salary * multiplier
        print(f"  ${salary:,} -> No Raise: ${if_no_raise:,.2f}, Needed: ${needed:,.2f}")

print("\n" + "="*80)
print("NOW I NEED TO VERIFY QQQ PRICES")
print("="*80)

print("\nQQQ prices I used:")
for date, price in QQQ_PRICES.items():
    print(f"  {date}: ${price}")

print("\nNEED TO VERIFY: Are these QQQ prices accurate?")
print("Especially Nov 2025 = $610 - is this the current price?")
