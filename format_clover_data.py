# -*- coding: utf-8 -*-
"""
@author: ryanc
"""

import pandas as pd
import re

def clean_currency_string(value):
    """Convert ($xx.xx) or $xx.xx to float"""
    if pd.isna(value): return 0.0
    value = str(value).strip()
    if value.startswith('(') and value.endswith(')'):
        value = '-' + value[1:-1]
    value = value.replace('$', '').replace(',', '').strip()
    try:
        return float(value)
    except:
        return 0.0

def clean_percent_string(value):
    """Convert 12.69% to 0.1269"""
    if pd.isna(value): return 0.0
    value = str(value).replace('%', '').strip()
    try:
        return float(value) / 100
    except:
        return 0.0

def format_clover_cleaned_v2(input_path, output_path):
    df = pd.read_csv(input_path)

    # Identify columns
    currency_cols = ['Gross Sales', 'Net Sales', 'Discounts', 'Repayments', 'Refunds', 'COGS', 'Gross Profit']
    percent_cols = ['% Net Sales']
    float_cols = ['Avg Item Size']
    int_cols = ['Sold']

    # Apply formatting
    for col in currency_cols:
        if col in df.columns:
            df[col] = df[col].apply(clean_currency_string)

    for col in percent_cols:
        if col in df.columns:
            df[col] = df[col].apply(clean_percent_string)

    for col in float_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col].apply(clean_currency_string), errors='coerce')

    for col in int_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

    # Save result
    df.to_csv(output_path, index=False)
    print(f"Formatted file saved to: {output_path}")

# Example usage
if __name__ == "__main__":
    format_clover_cleaned_v2("December Red Cleaned.csv",
                             "December Red Cleaned Formatted.csv")