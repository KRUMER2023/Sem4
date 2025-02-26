import csv

def calculate_average(csv_filename, column_name):
    try:
        with open(csv_filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            values = []
            for row in reader:
                try:
                    values.append(float(row[column_name]))
                except ValueError:
                    print(f"Skipping invalid value: {row[column_name]}")
            
            if values:
                return sum(values) / len(values)
            else:
                return "No valid numeric values found in the specified column."
    except FileNotFoundError:
        return "Error: File not found."
    except KeyError:
        return "Error: Column name not found in CSV."

# Example usage
csv_filename = "data.csv"
column_name = "Price"  # Change this to the target column name
average = calculate_average(csv_filename, column_name)
print(f"Average of column '{column_name}': {average}")