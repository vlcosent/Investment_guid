#!/usr/bin/env python3
"""
Update all slide values in the PowerPoint XML files
"""

import xml.etree.ElementTree as ET
import os

# Register namespaces
namespaces = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main'
}

for prefix, uri in namespaces.items():
    ET.register_namespace(prefix, uri)

# ===== UPDATE DATA =====

# Purchasing power of savings (Slides 13-16)
savings_updates = {
    13: {  # 5 years ago
        'title': '5 YEARS AGO (November 2020)',
        'data': [
            ('$5,000', '$4,131.47', '-$868.53'),
            ('$10,000', '$8,262.94', '-$1,737.06'),
            ('$25,000', '$20,657.35', '-$4,342.65'),
            ('$50,000', '$41,314.70', '-$8,685.30'),
        ]
    },
    14: {  # 10 years ago
        'title': '10 YEARS AGO (November 2015)',
        'data': [
            ('$5,000', '$3,767.86', '-$1,232.14'),
            ('$10,000', '$7,535.73', '-$2,464.27'),
            ('$25,000', '$18,839.31', '-$6,160.69'),
            ('$50,000', '$37,678.63', '-$12,321.37'),
        ]
    },
    15: {  # 20 years ago
        'title': '20 YEARS AGO (November 2005)',
        'data': [
            ('$5,000', '$3,137.50', '-$1,862.50'),
            ('$10,000', '$6,275.01', '-$3,724.99'),
            ('$25,000', '$15,687.52', '-$9,312.48'),
            ('$50,000', '$31,375.04', '-$18,624.96'),
        ]
    },
    16: {  # 30 years ago
        'title': '30 YEARS AGO (November 1995)',
        'data': [
            ('$5,000', '$2,438.87', '-$2,561.13'),
            ('$10,000', '$4,877.74', '-$5,122.26'),
            ('$25,000', '$12,194.35', '-$12,805.65'),
            ('$50,000', '$24,388.69', '-$25,611.31'),
        ]
    }
}

# Salary adjustments (Slides 18-21)
salary_updates = {
    18: {  # 5 years ago
        'title': '5 YEARS AGO (November 2020)',
        'data': [
            ('$50,000', '$41,314.70', '$60,511.15'),
            ('$65,000', '$53,709.11', '$78,664.49'),
            ('$80,000', '$66,103.52', '$96,817.83'),
            ('$100,000', '$82,629.41', '$121,022.29'),
        ]
    },
    19: {  # 10 years ago
        'title': '10 YEARS AGO (November 2015)',
        'data': [
            ('$50,000', '$37,678.63', '$66,350.61'),
            ('$65,000', '$48,982.22', '$86,255.79'),
            ('$80,000', '$60,285.81', '$106,160.98'),
            ('$100,000', '$75,357.26', '$132,701.22'),
        ]
    },
    20: {  # 20 years ago
        'title': '20 YEARS AGO (November 2005)',
        'data': [
            ('$50,000', '$31,375.04', '$79,681.17'),
            ('$65,000', '$40,787.55', '$103,585.53'),
            ('$80,000', '$50,200.06', '$127,489.88'),
            ('$100,000', '$62,750.08', '$159,362.35'),
        ]
    },
    21: {  # 30 years ago
        'title': '30 YEARS AGO (November 1995)',
        'data': [
            ('$50,000', '$24,388.69', '$102,506.51'),
            ('$65,000', '$31,705.30', '$133,258.46'),
            ('$80,000', '$39,021.91', '$164,010.42'),
            ('$100,000', '$48,777.39', '$205,013.02'),
        ]
    }
}

# Lump sum investments (Slides 34-37)
lump_sum_updates = {
    34: {  # 5 years
        'title': '5 Years Ago (Nov 2020 - Nov 2025)',
        'data': [
            ('$5,000', '$4,131.47', '$10,553.63'),
            ('$10,000', '$8,262.94', '$21,107.27'),
            ('$25,000', '$20,657.35', '$52,768.17'),
            ('$50,000', '$41,314.70', '$105,536.33'),
        ]
    },
    35: {  # 10 years
        'title': '10 Years Ago (Nov 2015 - Nov 2025)',
        'data': [
            ('$5,000', '$3,767.86', '$27,232.14'),
            ('$10,000', '$7,535.73', '$54,464.29'),
            ('$25,000', '$18,839.31', '$136,160.71'),
            ('$50,000', '$37,678.63', '$272,321.43'),
        ]
    },
    36: {  # 20 years
        'title': '20 Years Ago (Nov 2005 - Nov 2025)',
        'data': [
            ('$5,000', '$3,137.50', '$77,215.19'),
            ('$10,000', '$6,275.01', '$154,430.38'),
            ('$25,000', '$15,687.52', '$386,075.95'),
            ('$50,000', '$31,375.04', '$772,151.90'),
        ]
    },
    37: {  # 30 years
        'title': '30 Years Ago (Nov 1995 - Nov 2025)',
        'data': [
            ('$5,000', '$2,438.87', '$177,705.98'),
            ('$10,000', '$4,877.74', '$355,411.95'),
            ('$25,000', '$12,194.35', '$888,529.89'),
            ('$50,000', '$24,388.69', '$1,777,059.77'),
        ]
    }
}

# Monthly DCA investments (Slides 39-42)
dca_updates = {
    39: {  # 5 years
        'title': '5 Years Ago (Nov 2020 - Nov 2025)',
        'data': [
            ('$100', '$6,000.00', '$4,957.76', '$8,573.35'),
            ('$250', '$15,000.00', '$12,394.41', '$21,433.38'),
            ('$500', '$30,000.00', '$24,788.82', '$42,866.77'),
            ('$1,000', '$60,000.00', '$49,577.64', '$85,733.53'),
        ]
    },
    40: {  # 10 years
        'title': '10 Years Ago (Nov 2015 - Nov 2025)',
        'data': [
            ('$100', '$12,000.00', '$9,042.87', '$25,137.82'),
            ('$250', '$30,000.00', '$22,607.18', '$62,844.54'),
            ('$500', '$60,000.00', '$45,214.35', '$125,689.09'),
            ('$1,000', '$120,000.00', '$90,428.71', '$251,378.17'),
        ]
    },
    41: {  # 20 years
        'title': '20 Years Ago (Nov 2005 - Nov 2025)',
        'data': [
            ('$100', '$24,000.00', '$15,060.02', '$70,970.00'),
            ('$250', '$60,000.00', '$37,650.05', '$177,424.99'),
            ('$500', '$120,000.00', '$75,300.10', '$354,849.98'),
            ('$1,000', '$240,000.00', '$150,600.19', '$709,699.97'),
        ]
    },
    42: {  # 30 years
        'title': '30 Years Ago (Nov 1995 - Nov 2025)',
        'data': [
            ('$100', '$36,000.00', '$17,559.86', '$134,021.85'),
            ('$250', '$90,000.00', '$43,899.65', '$335,054.63'),
            ('$500', '$180,000.00', '$87,799.30', '$670,109.27'),
            ('$1,000', '$360,000.00', '$175,598.60', '$1,340,218.53'),
        ]
    }
}

def replace_text_in_slide(slide_num, replacements):
    """Replace text in a slide XML file"""
    slide_path = f'pptx_extracted/ppt/slides/slide{slide_num}.xml'

    if not os.path.exists(slide_path):
        print(f"Warning: {slide_path} not found")
        return False

    # Read the entire file content
    with open(slide_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Make replacements
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            print(f"  Replaced '{old}' with '{new}'")
        else:
            print(f"  Warning: Could not find '{old}' in slide {slide_num}")

    # Write back
    with open(slide_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

# Update slides 13-16 (Savings)
print("Updating Savings Slides (13-16)...")
for slide_num, update_info in savings_updates.items():
    print(f"\nSlide {slide_num}:")
    replacements = []

    # Update title if needed
    # Note: titles might not need updating

    # Update data values
    # The format in the slides is typically:
    # Original Amount: $5,000
    # Value Today: $4,021.84
    # Loss: -$978.16

    # We'll replace the specific old values with new ones
    # This requires careful matching of the old values

    replace_text_in_slide(slide_num, replacements)

print("\n" + "="*70)
print("Note: Manual verification of slides may be needed.")
print("Creating a more targeted update approach...")
print("="*70)

# Output all new values for reference
print("\n\n=== NEW VALUES FOR SLIDES ===\n")
print("SLIDES 13-16 (Purchasing Power of Savings):")
for slide_num, info in savings_updates.items():
    print(f"\nSlide {slide_num}: {info['title']}")
    for orig, value, loss in info['data']:
        print(f"  {orig} -> {value} (Loss: {loss})")

print("\n\nSLIDES 18-21 (Salary Adjustments):")
for slide_num, info in salary_updates.items():
    print(f"\nSlide {slide_num}: {info['title']}")
    for orig, no_raise, needed in info['data']:
        print(f"  {orig} -> No Raise: {no_raise}, Needed: {needed}")

print("\n\nSLIDES 34-37 (Lump Sum Investments):")
for slide_num, info in lump_sum_updates.items():
    print(f"\nSlide {slide_num}: {info['title']}")
    for amount, cash, investment in info['data']:
        print(f"  {amount} -> Cash: {cash}, Investment: {investment}")

print("\n\nSLIDES 39-42 (Monthly DCA Investments):")
for slide_num, info in dca_updates.items():
    print(f"\nSlide {slide_num}: {info['title']}")
    for monthly, total, cash, investment in info['data']:
        print(f"  {monthly}/month -> Total: {total}, Cash: {cash}, Investment: {investment}")
