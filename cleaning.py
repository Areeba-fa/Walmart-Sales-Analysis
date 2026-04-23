import pandas as pd

# Now we load the CLEANED file we just made
df = pd.read_csv('Walmart_Cleaned.csv')

# Find the total number of duplicate rows
duplicate_count = df.duplicated().sum()

print("--- DUPLICATE CHECK ---")
print(f"Total duplicate rows found: {duplicate_count}")

if duplicate_count > 0:
    df = df.drop_duplicates()
    df.to_csv('Walmart_Cleaned.csv', index=False)
    print("Duplicates removed and file updated!")
else:
    print("No duplicates found. Your data is unique!")