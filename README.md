Iconik Coffee Roasters uses the POS system Clover for its cafe sales. While Clover has some basic built-in analysis tools, they have limitations which have become apparent in Iconik's pursuit of a more sophisticated value-based pricing strategy. Unfortunately, Clover's data cloud is notorious for exporting poorly structured, junk-filled csv files that are not easily uploaded to query platforms like BigQuery. To avoid a mountain of effort spent manually cleaning exported Clover sales files, I've written a Python script that automatically preps these files, specifically for upload into BigQuery.

### Find the script [HERE](https://github.com/ryanloveriner/clover_to_postgresql_automators/blob/clover_cleaner/clean_clover_report.py)

### Please note:
1) Make sure to fill in the name of the file you want to clean on line 49 and your desired output file name on line 50.

2) The file you want to clean needs to be in the same place as the Python file.

3) You'll need to run the file from your terminal.
