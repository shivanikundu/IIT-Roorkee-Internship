#Load a CSV into Pandas ; display info() , describe() , handle missing values
import pandas as pd

# Step 1: Create sample data
data = {
    "Name": ["Varsha", "Chetna", "Udita", "Vandana"],
    "Age": [20, 21, None, 22],
    "Marks": [85, 90, 78, None]
}
# Step 2: Convert data into DataFrame
df = pd.DataFrame(data)

# Step 3: Save DataFrame to CSV
df.to_csv("students.csv", index=False)

print("CSV file created successfully!\n")

# Step 4: Load CSV file
df = pd.read_csv("students.csv")

# Step 5: Display data
print("Original Data:")
print(df)

# Step 6: Display information about the dataset
print("\nDataset Information:")
df.info()

# Step 7: Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Step 8: Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 9: Handle missing values by filling with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Step 10: Display updated data
print("\nData After Handling Missing Values:")
print(df)

# Optional: Save cleaned data
df.to_csv("students_cleaned.csv", index=False)

print("\nCleaned data saved to 'students_cleaned.csv'")