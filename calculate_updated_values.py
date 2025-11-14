#!/usr/bin/env python3
"""
Calculate updated values for purchasing power analysis presentation
Based on latest CPI and NASDAQ-100 data (November 2025)
"""

import math

# ===== DATA SOURCES =====
# CPI Data from FRED (CPIAUCSL)
CPI = {
    'Nov 1995': 153.6,
    'Nov 2005': 197.6,
    'Nov 2015': 237.3,
    'Nov 2020': 260.2,
    'Nov 2024': 314.9,  # Latest available
}

# QQQ Historical Prices (split-adjusted)
QQQ_PRICES = {
    'Nov 2005': 39.50,
    'Nov 2015': 112.00,
    'Nov 2020': 289.00,
    'Nov 2025': 610.00,  # Current
}

# Nasdaq-100 Index for 1995 (QQQ didn't exist)
NASDAQ100_1995 = 619
NASDAQ100_2025 = 22000

# ===== INFLATION CALCULATIONS =====
def calculate_inflation_metrics(old_cpi, new_cpi, years):
    """Calculate all inflation-related metrics"""
    multiplier = new_cpi / old_cpi
    cumulative_inflation = (multiplier - 1) * 100
    annual_rate = (pow(multiplier, 1/years) - 1) * 100

    return {
        'multiplier': multiplier,
        'cumulative_pct': cumulative_inflation,
        'annual_rate_pct': annual_rate
    }

def purchasing_power_table(amounts, old_cpi, new_cpi):
    """Calculate purchasing power for different amounts"""
    multiplier = new_cpi / old_cpi
    results = []
    for amount in amounts:
        value_today = amount / multiplier
        loss = amount - value_today
        results.append({
            'original': amount,
            'value_today': value_today,
            'loss': loss
        })
    return results

def salary_table(salaries, old_cpi, new_cpi):
    """Calculate needed salary adjustments"""
    multiplier = new_cpi / old_cpi
    results = []
    for salary in salaries:
        if_no_raise = salary / multiplier
        needed_salary = salary * multiplier
        results.append({
            'original': salary,
            'if_no_raise': if_no_raise,
            'needed': needed_salary
        })
    return results

# ===== INVESTMENT RETURN CALCULATIONS =====
def lump_sum_returns(amounts, start_price, end_price):
    """Calculate lump sum investment returns"""
    multiplier = end_price / start_price
    results = []
    for amount in amounts:
        investment_value = amount * multiplier
        results.append({
            'initial': amount,
            'final': investment_value,
            'multiplier': multiplier
        })
    return results

def dca_returns_estimate(monthly_amount, months, start_price, end_price):
    """
    Estimate DCA returns using simplified model
    Assumes linear price growth (not accurate but reasonable approximation)
    """
    total_invested = monthly_amount * months
    total_shares = 0

    # Simulate monthly purchases with linear price interpolation
    for month in range(months):
        price = start_price + (end_price - start_price) * (month / months)
        shares = monthly_amount / price
        total_shares += shares

    final_value = total_shares * end_price
    return {
        'monthly': monthly_amount,
        'total_invested': total_invested,
        'final_value': final_value
    }

# ===== GENERATE ALL CALCULATIONS =====

print("=" * 70)
print("PURCHASING POWER ANALYSIS - UPDATED VALUES")
print("November 2025")
print("=" * 70)

# Current CPI
current_cpi = CPI['Nov 2024']

# Define time periods
periods = [
    (5, 'Nov 2020', CPI['Nov 2020'], QQQ_PRICES['Nov 2020'], QQQ_PRICES['Nov 2025']),
    (10, 'Nov 2015', CPI['Nov 2015'], QQQ_PRICES['Nov 2015'], QQQ_PRICES['Nov 2025']),
    (20, 'Nov 2005', CPI['Nov 2005'], QQQ_PRICES['Nov 2005'], QQQ_PRICES['Nov 2025']),
    (30, 'Nov 1995', CPI['Nov 1995'], None, None),  # Use Nasdaq-100 index ratio
]

print("\n" + "=" * 70)
print("INFLATION DATA (Slide 11)")
print("=" * 70)

# Use 5-year data for Slide 11 example
years, date, old_cpi, old_price, new_price = periods[0]
metrics = calculate_inflation_metrics(old_cpi, current_cpi, years)

print(f"\nExample: {years} years ago ({date} to Nov 2024)")
print(f"1. Price Multiplier = {metrics['multiplier']:.4f}")
print(f"2. Cumulative Inflation % = {metrics['cumulative_pct']:.2f}%")
print(f"3. Annual Avg Rate % = {metrics['annual_rate_pct']:.2f}%")
print(f"4. Purchasing Power Today ($) = ${10/metrics['multiplier']:.2f} (for $10 historical)")
print(f"5. Purchasing Power Erosion % = {(1 - 1/metrics['multiplier'])*100:.2f}%")
print(f"6. Amount Needed Today = ${10 * metrics['multiplier']:.2f}")

print("\n" + "=" * 70)
print("PURCHASING POWER OF SAVINGS (Slides 13-16)")
print("=" * 70)

savings_amounts = [5000, 10000, 25000, 50000]

for years, date, old_cpi, _, _ in periods:
    print(f"\n{years} YEARS AGO ({date})")
    results = purchasing_power_table(savings_amounts, old_cpi, current_cpi)
    for r in results:
        print(f"${r['original']:,} -> ${r['value_today']:,.2f} (Loss: ${r['loss']:,.2f})")

print("\n" + "=" * 70)
print("SALARY ADJUSTMENTS NEEDED (Slides 18-21)")
print("=" * 70)

salaries = [50000, 65000, 80000, 100000]

for years, date, old_cpi, _, _ in periods:
    print(f"\n{years} YEARS AGO ({date})")
    results = salary_table(salaries, old_cpi, current_cpi)
    for r in results:
        print(f"${r['original']:,} -> If No Raise: ${r['if_no_raise']:,.2f}, Needed: ${r['needed']:,.2f}")

print("\n" + "=" * 70)
print("LUMP SUM INVESTMENT RETURNS (Slides 34-37)")
print("=" * 70)

investment_amounts = [5000, 10000, 25000, 50000]

for years, date, old_cpi, old_price, new_price in periods[:3]:  # First 3 periods with QQQ data
    print(f"\n{years} YEARS AGO ({date} to Nov 2025)")
    results = lump_sum_returns(investment_amounts, old_price, new_price)
    multiplier = metrics['multiplier'] if years == 5 else calculate_inflation_metrics(old_cpi, current_cpi, years)['multiplier']

    for r in results:
        cash_value = r['initial'] / multiplier
        print(f"${r['initial']:,} -> Cash: ${cash_value:,.2f}, Investment: ${r['final']:,.2f}")

# 30 years with Nasdaq-100 index ratio
print(f"\n30 YEARS AGO (Nov 1995 to Nov 2025)")
nasdaq_multiplier = NASDAQ100_2025 / NASDAQ100_1995
results = lump_sum_returns(investment_amounts, 1, nasdaq_multiplier)
old_cpi_30 = CPI['Nov 1995']
multiplier_30 = calculate_inflation_metrics(old_cpi_30, current_cpi, 30)['multiplier']

for r in results:
    cash_value = r['initial'] / multiplier_30
    print(f"${r['initial']:,} -> Cash: ${cash_value:,.2f}, Investment: ${r['final']:,.2f}")

print("\n" + "=" * 70)
print("MONTHLY DCA INVESTMENT RETURNS (Slides 39-42)")
print("=" * 70)

monthly_amounts = [100, 250, 500, 1000]

for years, date, old_cpi, old_price, new_price in periods[:3]:
    print(f"\n{years} YEARS ({date} to Nov 2025)")
    months = years * 12

    for monthly in monthly_amounts:
        result = dca_returns_estimate(monthly, months, old_price, new_price)
        multiplier = calculate_inflation_metrics(old_cpi, current_cpi, years)['multiplier']
        cash_value = result['total_invested'] / multiplier

        print(f"${monthly}/month -> Total: ${result['total_invested']:,}, "
              f"Cash: ${cash_value:,.2f}, Investment: ${result['final_value']:,.2f}")

# 30 years DCA
print(f"\n30 YEARS (Nov 1995 to Nov 2025)")
months = 30 * 12
# Use proportional scaling for Nasdaq-100
for monthly in monthly_amounts:
    result = dca_returns_estimate(monthly, months, 1, nasdaq_multiplier)
    multiplier_30 = calculate_inflation_metrics(CPI['Nov 1995'], current_cpi, 30)['multiplier']
    cash_value = result['total_invested'] / multiplier_30

    print(f"${monthly}/month -> Total: ${result['total_invested']:,}, "
          f"Cash: ${cash_value:,.2f}, Investment: ${result['final_value']:,.2f}")

print("\n" + "=" * 70)
print("CALCULATIONS COMPLETE")
print("=" * 70)
