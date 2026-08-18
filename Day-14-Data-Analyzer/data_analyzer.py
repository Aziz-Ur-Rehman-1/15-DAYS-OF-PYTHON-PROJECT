import csv
import os
import statistics
from collections import Counter
from datetime import datetime

def load_csv(file_path):
    if not os.path.exists(file_path):
        print(f"\nError: File '{file_path}' not found!\n")
        return None, None
    
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = list(csv.reader(file))
            if not reader:
                print("\nError: CSV file is empty!\n")
                return None, None
            
            headers = [h.strip() for h in reader[0]]
            data = reader[1:]
            return headers, data
    except Exception as e:
        print(f"\nError reading CSV file: {e}\n")
        return None, None

def analyze_column(headers, data, col_index):
    col_name = headers[col_index]
    values = [row[col_index].strip() for row in data if len(row) > col_index and row[col_index].strip() != ""]
    
    total_rows = len(data)
    missing_values = total_rows - len(values)
    
    # Check if column values are numeric
    numeric_values = []
    for v in values:
        try:
            numeric_values.append(float(v))
        except ValueError:
            pass
            
    is_numeric = len(numeric_values) == len(values) and len(values) > 0

    report_lines = []
    report_lines.append("=" * 55)
    report_lines.append(f"           ANALYSIS FOR COLUMN: '{col_name}'           ")
    report_lines.append("=" * 55)
    report_lines.append(f" Total Rows         : {total_rows}")
    report_lines.append(f" Non-Empty Values   : {len(values)}")
    report_lines.append(f" Missing Values     : {missing_values}")
    report_lines.append("-" * 55)

    if is_numeric:
        report_lines.append(" Data Type          : Numeric (Numbers)")
        report_lines.append(f" Minimum Value      : {min(numeric_values)}")
        report_lines.append(f" Maximum Value      : {max(numeric_values)}")
        report_lines.append(f" Average (Mean)     : {round(statistics.mean(numeric_values), 2)}")
        report_lines.append(f" Median Value       : {round(statistics.median(numeric_values), 2)}")
    else:
        report_lines.append(" Data Type          : Categorical (Text)")
        counts = Counter(values)
        report_lines.append(" Top Most Frequent Values:")
        for val, count in counts.most_common(5):
            report_lines.append(f"   - '{val}': {count} times")
            
    report_lines.append("=" * 55 + "\n")

    report_text = "\n".join(report_lines)
    print("\n" + report_text)
    return report_text

def export_summary_report(filename, report_content):
    try:
        log_file = "data_analysis_summary.txt"
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"\n--- Analysis Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
            f.write(f"Source File: {filename}\n")
            f.write(report_content)
        print(f"Success: Report exported to '{os.path.abspath(log_file)}'\n")
    except Exception as e:
        print(f"Error exporting report: {e}\n")

def main():
    loaded_file = None
    headers = None
    data = None

    while True:
        print("--- CSV DATA ANALYZER & INSIGHTS GENERATOR ---")
        print("1. Load CSV File")
        print("2. Analyze Specific Column")
        print("3. View Dataset Summary (Overview)")
        print("4. Exit")

        choice = input("\nEnter choice (1-4): ").strip()

        if choice == "1":
            path = input("Enter CSV file path (e.g. sales_data.csv): ").strip()
            h, d = load_csv(path)
            if h and d:
                loaded_file = path
                headers = h
                data = d
                print(f"\nSuccess: Loaded '{path}' with {len(headers)} columns and {len(data)} rows.\n")

        elif choice == "2":
            if not loaded_file:
                print("\nPlease load a CSV file first (Option 1)!\n")
                continue

            print("\nAvailable Columns:")
            for idx, name in enumerate(headers):
                print(f"  [{idx}] {name}")
            
            try:
                col_idx = int(input(f"\nEnter Column Index (0 to {len(headers)-1}): "))
                if 0 <= col_idx < len(headers):
                    report = analyze_column(headers, data, col_idx)
                    save_choice = input("Do you want to save this analysis report? (y/n): ").strip().lower()
                    if save_choice == 'y':
                        export_summary_report(loaded_file, report)
                else:
                    print("\nInvalid Column Index!\n")
            except ValueError:
                print("\nPlease enter a valid number!\n")

        elif choice == "3":
            if not loaded_file:
                print("\nPlease load a CSV file first (Option 1)!\n")
                continue

            print("\n" + "=" * 55)
            print("                DATASET OVERVIEW                ")
            print("=" * 55)
            print(f" File Name     : {loaded_file}")
            print(f" Total Rows    : {len(data)}")
            print(f" Total Columns : {len(headers)}")
            print(f" Columns List  : {', '.join(headers)}")
            print("=" * 55 + "\n")

        elif choice == "4":
            print("\nGoodbye!\n")
            break
        else:
            print("\nInvalid choice. Try again!\n")

if __name__ == "__main__":
    main()