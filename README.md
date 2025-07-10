The second step of the Clover to DBeaver pipeline formats the numerical columns of the cleaned clover reports in a PostgreSQL-friendly way.

### Find the script [HERE](https://github.com/ryanloveriner/clover_to_postgresql_automators/blob/clover_formatter/format_clover_data.py)

### Please note:
1) This script is designed to be used specifically on csv files that have been cleaned using the [automated cleaner](https://github.com/ryanloveriner/clover_to_postgresql_automators/blob/clover_cleaner/clean_clover_report.py)

2) Make sure to fill in the name of the file you want to clean on line 45 and your desired output file name on line 46.

3) The file you want to clean needs to be in the same folder as the Python file.

4) You'll need to run the file from your terminal.
