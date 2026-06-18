#Mini EDA : filter , group by , and plot a bar chart
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create sample data
data = {
    "Name": ["Varsha", "Chetna", "Vandana", "Vishavbharti", "Udita"],
    "Department": ["CSE", "CSE", "ECE", "ECE", "CSE"],
    "Marks": [85, 90, 78, 88, 92]
}

df = pd.DataFrame(data)

# Step 2: Save to CSV
df.to_csv("students.csv", index=False)

# Step 3: Load CSV
df = pd.read_csv("students.csv")

print("Original Data:")
print(df)

# Step 4: Filter students with marks > 85
filtered = df[df["Marks"] > 85]

print("\nStudents with Marks > 85:")
print(filtered)

# Step 5: Group by Department and calculate average marks
grouped = df.groupby("Department")["Marks"].mean()

print("\nAverage Marks by Department:")
print(grouped)

# Step 6: Plot Bar Chart
grouped.plot(kind="bar")

plt.title("Average Marks by Department")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.show()