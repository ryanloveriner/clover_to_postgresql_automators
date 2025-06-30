# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 16:50:25 2025

@author: ryanc
"""

import pandas as pd
from io import StringIO

def clean_clover_csv(input_csv_path, output_csv_path):
    # Read file as text to locate the actual header row
    with open(input_csv_path, 'r', encoding='utf-8') as file:
        raw_lines = file.readlines()

    # Find header row
    header_line_index = None
    for i, line in enumerate(raw_lines):
        if "Category Name,Name,Gross Sales" in line:
            header_line_index = i
            break

    if header_line_index is None:
        raise ValueError("Could not locate the header row in the Clover report.")

    # Extract clean data starting from header
    clean_data_str = "".join(raw_lines[header_line_index:])
    clean_data_io = StringIO(clean_data_str)
    df = pd.read_csv(clean_data_io)

    # Drop modifier rows (which have values in 'Modifier Name')
    df = df[df['Modifier Name'].isna() | (df['Modifier Name'].str.strip() == '')]

    # Drop rows without a valid 'Name'
    df = df[df['Name'].notna() & (df['Name'].str.strip() != '')]

    # Drop unwanted columns
    df = df.drop(columns=['Modifier Name', 'Modifier Sold', 'Modifier Amount', 'Category Name'], errors='ignore')

    # Reset index
    df.reset_index(drop=True, inplace=True)

    # Save cleaned file
    df.to_csv(output_csv_path, index=False)
    print(f"Cleaned file saved to: {output_csv_path}")

# Example usage
if __name__ == "__main__":
    input_path = #FILE TO BE CLEANED
    output_path = #OUTPUT FILE NAME
    clean_clover_csv(input_path, output_path)
