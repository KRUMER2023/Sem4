import pandas as pd

def read_excel(file_name, sheet_name=0):
    try:
        # Read the Excel file
        df = pd.read_excel(file_name, sheet_name=sheet_name)
        # Print the data in a tabular format
        print(df.to_string(index=False))
    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError:
        print("Error: Invalid sheet name.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_name = "data.xlsx"  # Change this to your Excel file name
read_excel(file_name)
