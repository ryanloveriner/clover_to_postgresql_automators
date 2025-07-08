# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 11:11:03 2025

@author: ryanc
"""

import pandas as pd

def format_clover_cleaned(input_csv_path, output_csv_path):
    df = pd.read_csv(input_csv_path)

    # Define formatting rules
    currency_cols = ['Gross Sales', 'Net Sales', 'Discounts', 'Repayments', 'Refunds', 'COGS', 'Gross Profit']
    percent_cols = ['% Net Sales']
    float_cols = ['Avg Item Size']
    int_cols = ['Sold', 'Refunded']

    # Format currency columns: remove $, commas, convert to float
    for col in currency_cols:
        if col in df.columns:
            df[col] = df[col].replace('[\$,]', '', regex=True).astype(float)

    # Format percent columns: remove %, convert to proportion
    for col in percent_cols:
        if col in df.columns:
            df[col] = df[col].str.replace('%', '').astype(float) / 100

    # Format float columns
    for col in float_cols:
        if col in df.columns:
            df[col] = df[col].replace('[\$,]', '', regex=True).astype(float)

    # Format integer-like columns
    for col in int_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

    # Save output
    df.to_csv(output_csv_path, index=False)
    print(f"Formatted file saved to: {output_csv_path}")

# Example usage
if __name__ == "__main__":
    input_file = "February Lupe Cleaned.csv"
    output_file = "February Lupe Cleaned Formatted.csv"
    format_clover_cleaned(input_file, output_file)