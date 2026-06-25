
# Load the Titanic dataset, find and fill missing values
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#Load Titanic data set
df = sns.load_dataset("titanic")

#Find missing value
miss_val = df.isna().sum()
print("-----Total missing values before cleaning-----")
print(miss_val)

#Fill missing value -- Quantitative by their mean ,categorical by their mode
mode_embarked = df["embarked"].mode()[0]
mode_deck = df["deck"].mode()[0]
mode_embark_town = df["embark_town"].mode()[0]
mean_age = df["age"].mean()
fill_val={"age" : mean_age, "embarked" : mode_embarked, "deck" :mode_deck , "embark_town" : mode_embark_town}
df = df.fillna(value = fill_val , inplace = True)
print(df.isnull().sum())