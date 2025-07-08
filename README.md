Iconik Coffee Roasters uses the POS system Clover for its cafe sales. While Clover has some basic built-in analysis tools, they have limitations which have become apparent in Iconik's pursuit of a more sophisticated value-based pricing strategy. Unfortunately, Clover's data cloud is notorious for exporting poorly structured, junk-filled csv files that are not easily uploaded to query platforms like PostgreSQL. To avoid a mountain of effort spent manually cleaning exported Clover sales files, I've written a few Python scripts with the help of ChatGPT that automatically preps these files, specifically for upload into DBeaver.

### After you've exported an Item Sales Report from Clover:

### 1) [Clean the csv file with this python script](https://github.com/ryanloveriner/clover_data_cleaner/blob/main/clean_clover_report.py)

### 2) [Format the csv file with this one]()

### 3) [And automatically upload to DBeaver with this one]()
