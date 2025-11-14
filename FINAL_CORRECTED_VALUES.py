#!/usr/bin/env python3
"""
FINAL CORRECTED VALUES FOR ALL SLIDES
Using VERIFIED data:
- CPI Sep 2025: 324.368 (most recent available)
- QQQ Nov 2025: $609
"""

import math

# VERIFIED DATA
CPI = {
    'Nov 1995': 153.6,
    'Nov 2005': 197.6,
    'Nov 2015': 237.336,
    'Nov 2020': 260.229,
    'Sep 2025': 324.368,
}

QQQ = {
    'Nov 2005': 39.50,
    'Nov 2015': 112.00,
    'Nov 2020': 289.00,
    'Nov 2025': 609.00,
}

NASDAQ100_1995 = 619
NASDAQ100_2025 = 22000

current_cpi = CPI['Sep 2025']
current_qqq = QQQ['Nov 2025']

print("="*80)
print("COMPLETE CORRECTED VALUES FOR ALL SLIDES")
print("="*80)

# ========== SLIDE 11 ==========
print("\n" + "="*80)
print("SLIDE 11 - THE MATHEMATICS")
print("="*80)

old_cpi = CPI['Nov 2020']
years = 4.833
mult = current_cpi / old_cpi
cum = (mult - 1) * 100
ann = (pow(mult, 1/years) - 1) * 100

print(f"\n1. Price Multiplier = {current_cpi:.1f} / {old_cpi:.3f} = {mult:.6f} ≈ {mult:.2f}")
print(f"2. Cumulative Inflation % = {cum:.2f}%")
print(f"3. Annual Avg Rate % = {ann:.2f}%")
print(f"4. Purchasing Power Today ($) = ${10/mult:.2f}")
print(f"5. Purchasing Power Erosion % = {(1 - 1/mult)*100:.2f}%")
print(f"6. Amount Needed Today = ${10*mult:.2f}")

# ========== SLIDES 13-16: PURCHASING POWER OF SAVINGS ==========
print("\n" + "="*80)
print("SLIDES 13-16: PURCHASING POWER OF SAVINGS")
print("="*80)

periods = [
    (13, '5 YEARS AGO', 'November 2020', CPI['Nov 2020']),
    (14, '10 YEARS AGO', 'November 2015', CPI['Nov 2015']),
    (15, '20 YEARS AGO', 'November 2005', CPI['Nov 2005']),
    (16, '30 YEARS AGO', 'November 1995', CPI['Nov 1995']),
]

savings = [5000, 10000, 25000, 50000]

for slide_num, title, date, old_cpi in periods:
    mult = current_cpi / old_cpi
    print(f"\nSlide {slide_num}: {title} ({date})")
    for amount in savings:
        value_today = amount / mult
        loss = amount - value_today
        print(f"  ${amount:,} -> ${value_today:,.2f} (Loss: ${loss:,.2f})")

# ========== SLIDES 18-21: SALARY ADJUSTMENTS ==========
print("\n" + "="*80)
print("SLIDES 18-21: SALARY ADJUSTMENTS")
print("="*80)

salaries = [50000, 65000, 80000, 100000]

for slide_num, title, date, old_cpi in periods:
    if slide_num == 13: slide_num = 18
    elif slide_num == 14: slide_num = 19
    elif slide_num == 15: slide_num = 20
    elif slide_num == 16: slide_num = 21

    mult = current_cpi / old_cpi
    print(f"\nSlide {slide_num}: {title} ({date})")
    for salary in salaries:
        if_no_raise = salary / mult
        needed = salary * mult
        print(f"  ${salary:,} -> No Raise: ${if_no_raise:,.2f}, Needed: ${needed:,.2f}")

# ========== SLIDES 34-37: LUMP SUM INVESTMENTS ==========
print("\n" + "="*80)
print("SLIDES 34-37: LUMP SUM INVESTMENTS")
print("="*80)

lump_periods = [
    (34, '5 Years Ago', 'Nov 2020', CPI['Nov 2020'], QQQ['Nov 2020'], QQQ['Nov 2025']),
    (35, '10 Years Ago', 'Nov 2015', CPI['Nov 2015'], QQQ['Nov 2015'], QQQ['Nov 2025']),
    (36, '20 Years Ago', 'Nov 2005', CPI['Nov 2005'], QQQ['Nov 2005'], QQQ['Nov 2025']),
]

amounts = [5000, 10000, 25000, 50000]

for slide_num, title, date, old_cpi, old_qqq, new_qqq in lump_periods:
    cpi_mult = current_cpi / old_cpi
    qqq_mult = new_qqq / old_qqq
    print(f"\nSlide {slide_num}: {title} ({date} - Nov 2025)")
    for amount in amounts:
        cash_value = amount / cpi_mult
        inv_value = amount * qqq_mult
        print(f"  ${amount:,} -> Cash: ${cash_value:,.2f}, Investment: ${inv_value:,.2f}")

# Slide 37: 30 years (Nasdaq-100 index)
nasdaq_mult = NASDAQ100_2025 / NASDAQ100_1995
cpi_mult_30 = current_cpi / CPI['Nov 1995']
print(f"\nSlide 37: 30 Years Ago (Nov 1995 - Nov 2025)")
for amount in amounts:
    cash_value = amount / cpi_mult_30
    inv_value = amount * nasdaq_mult
    print(f"  ${amount:,} -> Cash: ${cash_value:,.2f}, Investment: ${inv_value:,.2f}")

# ========== SLIDES 39-42: MONTHLY DCA INVESTMENTS ==========
print("\n" + "="*80)
print("SLIDES 39-42: MONTHLY DCA INVESTMENTS")
print("="*80)

def calculate_dca(monthly, months, start_price, end_price):
    """Calculate DCA returns"""
    total_invested = monthly * months
    total_shares = 0
    for month in range(months):
        price = start_price + (end_price - start_price) * (month / months)
        shares = monthly / price
        total_shares += shares
    final_value = total_shares * end_price
    return total_invested, final_value

monthly_amounts = [100, 250, 500, 1000]

dca_periods = [
    (39, '5 Years', 'Nov 2020', CPI['Nov 2020'], QQQ['Nov 2020'], QQQ['Nov 2025'], 60),
    (40, '10 Years', 'Nov 2015', CPI['Nov 2015'], QQQ['Nov 2015'], QQQ['Nov 2025'], 120),
    (41, '20 Years', 'Nov 2005', CPI['Nov 2005'], QQQ['Nov 2005'], QQQ['Nov 2025'], 240),
]

for slide_num, title, date, old_cpi, old_qqq, new_qqq, months in dca_periods:
    cpi_mult = current_cpi / old_cpi
    print(f"\nSlide {slide_num}: {title} Ago ({date} - Nov 2025)")
    for monthly in monthly_amounts:
        total_inv, final_val = calculate_dca(monthly, months, old_qqq, new_qqq)
        cash_value = total_inv / cpi_mult
        print(f"  ${monthly}/mo -> Total: ${total_inv:,.2f}, Cash: ${cash_value:,.2f}, Invest: ${final_val:,.2f}")

# Slide 42: 30 years DCA
months_30 = 360
cpi_mult_30 = current_cpi / CPI['Nov 1995']
print(f"\nSlide 42: 30 Years Ago (Nov 1995 - Nov 2025)")
for monthly in monthly_amounts:
    total_inv, final_val = calculate_dca(monthly, months_30, 1, nasdaq_mult)
    cash_value = total_inv / cpi_mult_30
    print(f"  ${monthly}/mo -> Total: ${total_inv:,.2f}, Cash: ${cash_value:,.2f}, Invest: ${final_val:,.2f}")

print("\n" + "="*80)
print("CALCULATION COMPLETE")
print("="*80)
