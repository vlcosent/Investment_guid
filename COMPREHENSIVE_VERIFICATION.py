#!/usr/bin/env python3
"""
COMPREHENSIVE MATHEMATICAL VERIFICATION
Checking EVERY calculation in the presentation
"""

import math

print("="*80)
print("COMPREHENSIVE MATHEMATICAL VERIFICATION")
print("="*80)

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

errors = []

def check_value(description, expected, actual, tolerance=0.02):
    """Check if value matches within tolerance"""
    if abs(expected - actual) > tolerance:
        error = f"ERROR: {description}\n  Expected: ${expected:.2f}\n  Actual: ${actual:.2f}\n  Difference: ${abs(expected - actual):.2f}"
        errors.append(error)
        print(f"❌ {error}")
        return False
    else:
        print(f"✓ {description}: ${actual:.2f}")
        return True

print("\n" + "="*80)
print("SLIDE 11 - FORMULA VERIFICATION")
print("="*80)

# Slide 11 formulas
old_cpi_5yr = CPI['Nov 2020']
years_5yr = 5  # They use 5 years as approximation

mult = current_cpi / old_cpi_5yr
print(f"\n1. Price Multiplier:")
print(f"   324.368 / 260.229 = {mult:.6f}")
print(f"   Slide shows: 1.246471")
print(f"   ✓ CORRECT" if abs(mult - 1.246471) < 0.000001 else f"   ❌ ERROR: Should be {mult:.6f}")

cum_inf = (mult - 1) * 100
print(f"\n2. Cumulative Inflation:")
print(f"   ({mult:.6f} - 1) × 100 = {cum_inf:.2f}%")
print(f"   Slide shows: 24.65%")
print(f"   ✓ CORRECT" if abs(cum_inf - 24.65) < 0.01 else f"   ❌ ERROR")

ann_rate = (pow(mult, 1/years_5yr) - 1) * 100
print(f"\n3. Annual Average Rate:")
print(f"   ({mult:.6f})^(1/5) - 1) × 100 = {ann_rate:.2f}%")
print(f"   Slide shows: 4.66%")
print(f"   ✓ CORRECT" if abs(ann_rate - 4.66) < 0.01 else f"   ❌ ERROR")

purch_power = 10 / mult
print(f"\n4. Purchasing Power:")
print(f"   $10 / {mult:.6f} = ${purch_power:.2f}")
print(f"   Slide shows: $8.02")
print(f"   ✓ CORRECT" if abs(purch_power - 8.02) < 0.01 else f"   ❌ ERROR")

erosion = (1 - 1/mult) * 100
print(f"\n5. Purchasing Power Erosion:")
print(f"   (1 - 1/{mult:.6f}) × 100 = {erosion:.2f}%")
print(f"   Slide shows: 19.77%")
print(f"   ✓ CORRECT" if abs(erosion - 19.77) < 0.01 else f"   ❌ ERROR")

needed = 10 * mult
print(f"\n6. Amount Needed:")
print(f"   $10 × {mult:.6f} = ${needed:.2f}")
print(f"   Slide shows: $12.46")
print(f"   ✓ CORRECT" if abs(needed - 12.46) < 0.01 else f"   ❌ ERROR")

print("\n" + "="*80)
print("SLIDE 13 - 5 YEARS SAVINGS VERIFICATION")
print("="*80)

slide13_data = [
    (5000, 4011.32, -988.68),
    (10000, 8022.65, -1977.35),
    (25000, 20056.62, -4943.38),
    (50000, 40113.24, -9886.76),
]

mult_5yr = current_cpi / CPI['Nov 2020']
for original, value_shown, loss_shown in slide13_data:
    calc_value = original / mult_5yr
    calc_loss = original - calc_value

    print(f"\n${original:,}:")
    check_value(f"  Value Today", calc_value, value_shown)
    check_value(f"  Loss", calc_loss, abs(loss_shown))

print("\n" + "="*80)
print("SLIDE 14 - 10 YEARS SAVINGS VERIFICATION")
print("="*80)

slide14_data = [
    (5000, 3658.44, -1341.56),
    (10000, 7316.87, -2683.13),
    (25000, 18292.19, -6707.81),
    (50000, 36584.37, -13415.63),
]

mult_10yr = current_cpi / CPI['Nov 2015']
for original, value_shown, loss_shown in slide14_data:
    calc_value = original / mult_10yr
    calc_loss = original - calc_value

    print(f"\n${original:,}:")
    check_value(f"  Value Today", calc_value, value_shown)
    check_value(f"  Loss", calc_loss, abs(loss_shown))

print("\n" + "="*80)
print("SLIDE 15 - 20 YEARS SAVINGS VERIFICATION")
print("="*80)

slide15_data = [
    (5000, 3045.92, -1954.08),
    (10000, 6091.85, -3908.15),
    (25000, 15229.62, -9770.38),
    (50000, 30459.23, -19540.77),
]

mult_20yr = current_cpi / CPI['Nov 2005']
for original, value_shown, loss_shown in slide15_data:
    calc_value = original / mult_20yr
    calc_loss = original - calc_value

    print(f"\n${original:,}:")
    check_value(f"  Value Today", calc_value, value_shown)
    check_value(f"  Loss", calc_loss, abs(loss_shown))

print("\n" + "="*80)
print("SLIDE 16 - 30 YEARS SAVINGS VERIFICATION")
print("="*80)

slide16_data = [
    (5000, 2367.68, -2632.32),
    (10000, 4735.36, -5264.64),
    (25000, 11838.41, -13161.59),
    (50000, 23676.81, -26323.19),
]

mult_30yr = current_cpi / CPI['Nov 1995']
for original, value_shown, loss_shown in slide16_data:
    calc_value = original / mult_30yr
    calc_loss = original - calc_value

    print(f"\n${original:,}:")
    check_value(f"  Value Today", calc_value, value_shown)
    check_value(f"  Loss", calc_loss, abs(loss_shown))

print("\n" + "="*80)
print("SLIDE 18 - 5 YEARS SALARY VERIFICATION")
print("="*80)

slide18_data = [
    (50000, 40113.24, 62323.57),
    (65000, 52147.21, 81020.64),
    (80000, 64181.18, 99717.71),
    (100000, 80226.47, 124647.14),
]

for salary, no_raise_shown, needed_shown in slide18_data:
    calc_no_raise = salary / mult_5yr
    calc_needed = salary * mult_5yr

    print(f"\n${salary:,}:")
    check_value(f"  If No Raise", calc_no_raise, no_raise_shown)
    check_value(f"  Needed", calc_needed, needed_shown, tolerance=0.5)

print("\n" + "="*80)
print("SLIDE 19 - 10 YEARS SALARY VERIFICATION")
print("="*80)

slide19_data = [
    (50000, 36584.37, 68335.19),
    (65000, 47559.69, 88835.74),
    (80000, 58535.00, 109336.30),
    (100000, 73168.75, 136670.37),
]

for salary, no_raise_shown, needed_shown in slide19_data:
    calc_no_raise = salary / mult_10yr
    calc_needed = salary * mult_10yr

    print(f"\n${salary:,}:")
    check_value(f"  If No Raise", calc_no_raise, no_raise_shown)
    check_value(f"  Needed", calc_needed, needed_shown, tolerance=0.5)

print("\n" + "="*80)
print("SLIDE 20 - 20 YEARS SALARY VERIFICATION")
print("="*80)

slide20_data = [
    (50000, 30459.23, 82076.92),
    (65000, 39597.00, 106700.00),
    (80000, 48734.77, 131323.08),
    (100000, 60918.46, 164153.85),
]

for salary, no_raise_shown, needed_shown in slide20_data:
    calc_no_raise = salary / mult_20yr
    calc_needed = salary * mult_20yr

    print(f"\n${salary:,}:")
    check_value(f"  If No Raise", calc_no_raise, no_raise_shown)
    check_value(f"  Needed", calc_needed, needed_shown, tolerance=0.5)

print("\n" + "="*80)
print("SLIDE 21 - 30 YEARS SALARY VERIFICATION")
print("="*80)

slide21_data = [
    (50000, 23676.81, 105588.54),
    (65000, 30779.85, 137265.10),
    (80000, 37882.90, 168941.67),
    (100000, 47353.62, 211177.08),
]

for salary, no_raise_shown, needed_shown in slide21_data:
    calc_no_raise = salary / mult_30yr
    calc_needed = salary * mult_30yr

    print(f"\n${salary:,}:")
    check_value(f"  If No Raise", calc_no_raise, no_raise_shown)
    check_value(f"  Needed", calc_needed, needed_shown, tolerance=0.5)

print("\n" + "="*80)
print("SLIDE 34 - 5 YEARS LUMP SUM INVESTMENT VERIFICATION")
print("="*80)

slide34_data = [
    (5000, 4011.32, 10536.33),
    (10000, 8022.65, 21072.66),
    (25000, 20056.62, 52681.66),
    (50000, 40113.24, 105363.32),
]

qqq_mult_5yr = QQQ['Nov 2025'] / QQQ['Nov 2020']
print(f"QQQ Multiplier: {QQQ['Nov 2025']} / {QQQ['Nov 2020']} = {qqq_mult_5yr:.4f}")

for amount, cash_shown, inv_shown in slide34_data:
    calc_cash = amount / mult_5yr
    calc_inv = amount * qqq_mult_5yr

    print(f"\n${amount:,}:")
    check_value(f"  Cash Value", calc_cash, cash_shown)
    check_value(f"  Investment Value", calc_inv, inv_shown, tolerance=1.0)

print("\n" + "="*80)
print("SLIDE 35 - 10 YEARS LUMP SUM INVESTMENT VERIFICATION")
print("="*80)

slide35_data = [
    (5000, 3658.44, 27187.50),
    (10000, 7316.87, 54375.00),
    (25000, 18292.19, 135937.50),
    (50000, 36584.37, 271875.00),
]

qqq_mult_10yr = QQQ['Nov 2025'] / QQQ['Nov 2015']
print(f"QQQ Multiplier: {QQQ['Nov 2025']} / {QQQ['Nov 2015']} = {qqq_mult_10yr:.4f}")

for amount, cash_shown, inv_shown in slide35_data:
    calc_cash = amount / mult_10yr
    calc_inv = amount * qqq_mult_10yr

    print(f"\n${amount:,}:")
    check_value(f"  Cash Value", calc_cash, cash_shown)
    check_value(f"  Investment Value", calc_inv, inv_shown, tolerance=1.0)

print("\n" + "="*80)
print("SLIDE 36 - 20 YEARS LUMP SUM INVESTMENT VERIFICATION")
print("="*80)

slide36_data = [
    (5000, 3045.92, 77088.61),
    (10000, 6091.85, 154177.22),
    (25000, 15229.62, 385443.04),
    (50000, 30459.23, 770886.08),
]

qqq_mult_20yr = QQQ['Nov 2025'] / QQQ['Nov 2005']
print(f"QQQ Multiplier: {QQQ['Nov 2025']} / {QQQ['Nov 2005']} = {qqq_mult_20yr:.4f}")

for amount, cash_shown, inv_shown in slide36_data:
    calc_cash = amount / mult_20yr
    calc_inv = amount * qqq_mult_20yr

    print(f"\n${amount:,}:")
    check_value(f"  Cash Value", calc_cash, cash_shown)
    check_value(f"  Investment Value", calc_inv, inv_shown, tolerance=1.0)

print("\n" + "="*80)
print("SLIDE 37 - 30 YEARS LUMP SUM INVESTMENT VERIFICATION")
print("="*80)

slide37_data = [
    (5000, 2367.68, 177705.98),
    (10000, 4735.36, 355411.95),
    (25000, 11838.41, 888529.89),
    (50000, 23676.81, 1777059.77),
]

nasdaq_mult_30yr = NASDAQ100_2025 / NASDAQ100_1995
print(f"NASDAQ-100 Multiplier: {NASDAQ100_2025} / {NASDAQ100_1995} = {nasdaq_mult_30yr:.4f}")

for amount, cash_shown, inv_shown in slide37_data:
    calc_cash = amount / mult_30yr
    calc_inv = amount * nasdaq_mult_30yr

    print(f"\n${amount:,}:")
    check_value(f"  Cash Value", calc_cash, cash_shown)
    check_value(f"  Investment Value", calc_inv, inv_shown, tolerance=1.0)

print("\n" + "="*80)
print("VERIFICATION SUMMARY")
print("="*80)

if errors:
    print(f"\n❌ FOUND {len(errors)} ERRORS:")
    for error in errors:
        print(f"\n{error}")
else:
    print("\n✅ ALL CALCULATIONS VERIFIED CORRECT!")
