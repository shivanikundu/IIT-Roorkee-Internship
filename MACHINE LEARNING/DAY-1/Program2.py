
# Explore the Iris dataset: shape, describe, value_counts 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = sns.load_dataset("iris")
print(f"Shape of dataset : {df.shape}")
print(f"Statistical Summary (Describe) : {df.describe()}")
print(f"Value Counts (how many flowers of respective species) : {df['species'].value_counts()}")