# Evaluation of Challenges and Characteristics of Sustainable Self-Supply Water Systems

## Overview

This repository contains code for analyzing survey data on the practice of sustainable self-supply water systems. The analysis includes generating frequency tables, percentages, and chi-square goodness-of-fit tests for various demographic and water-related variables. It features:

- A Jupyter Notebook (`main2.ipynb`) for static analysis and exporting results to Excel.
- A Dash application (`main.py`) for an interactive dashboard to visualize distributions with pie charts and tables.


Key variables analyzed:
- Demographics: Gender, Age Group, Educational Level, Occupation.
- Water-related: Residency duration, Primary water source, Self-supply duration, Construction, Reasons for use, Shortages, Challenges, Waterborne diseases, Quality addressing methods, Suggested improvements.

## Requirements

- Python 3.10+
- Libraries:
  - pandas
  - scipy
  - dash
  - plotly
  - openpyxl (for Excel reading/writing)


## Usage

### Jupyter Notebook (`main2.ipynb`)
1. Open the notebook in Jupyter:
   ```
   jupyter notebook main2.ipynb
   ```
2. Run the cells to load data, analyze columns, generate a concatenated frequency table with p-values, and export to `demographic_table.xlsx`.

### Dash Dashboard (`main.py`)
1. Run the script:
   ```
   python main.py
   ```
2. Open http://127.0.0.1:8050/ in your browser.
3. Use the dropdown to select a variable and view its frequency table, p-value, and interactive pie chart.

## Screenshot
<img width="1360" height="726" alt="image" src="https://github.com/user-attachments/assets/fce5d38d-d1c7-4dcb-a5a6-f88cf4b97ebb" />



## Data Structure

The dataset has columns such as:
- "Gender"
- "Age Group"
- "Educational level"
- "Occupation"
- And various water supply questions (see code for full list).

The analysis performs:
- Frequency counts and percentages.
- Chi-square goodness-of-fit test assuming uniform distribution.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


