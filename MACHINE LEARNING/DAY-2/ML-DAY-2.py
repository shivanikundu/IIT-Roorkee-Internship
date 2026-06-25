'''********DAY-2*********'''
print("----------------PROGRAM-1------------------")
#PROGRAM-1
#Load the Titanic dataset, find and fill missing values
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.preprocessing import LabelEncoder ,  StandardScaler
from sklearn.model_selection import train_test_split
#Loding Dataset
df = sns.load_dataset("titanic")

#Cleaning Data

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
print("Data After cleaning is : \n" , df.head())


print("----------------PROGRAM-2------------------")
#PROGRAM-2
#Encode 'Sex' and 'Embarked' columns using LabelEncoder in Titanic dataset
choice = int(input("Enter choice(1-encode without using LabelEncoder and 2-encode using LabelEncoder) : "))
if choice == 1 :
    #Encode 'Sex' for "male"=0 and "Female"=1
    print(df['sex'].value_counts())
    df['sex'] = df['sex'].map({"male" : 0 , "female" : 1})

    #Encode 'Embarked' for "S"=0 , "C"=1 , "Q"=2
    print(df['embarked'].value_counts())
    df['embarked'] = df['embarked'].map({"S" : 0 , "C" : 1 , "Q" : 2})
    print("sex and embarked after encoded :")
    print(df[['sex', 'embarked']].head())
elif choice == 2 :
    # Initialize the label encoder
    le_sex = LabelEncoder()
    le_embarked = LabelEncoder()

    # Fit and transform the text columns into numeric columns
    df['sex'] = le_sex.fit_transform(df['sex'])
    df['embarked'] = le_embarked.fit_transform(df['embarked'].astype(str))
    print("sex and embarked after encoded : ")
    print(df[['sex', 'embarked']].head())
else :
    print("Invalid choice! ")

print("----------------PROGRAM-3------------------")
#PROGRAM_3
#Apply StandardScaler on Age and Fare columns in Titanic Dataset
scaler = StandardScaler()
df[['age', 'fare']] = scaler.fit_transform(df[['age', 'fare']])
print(df[['age', 'fare']].head())

print("----------------PROGRAM-4------------------")
#PROGRAM-4
#Split dataset 80/20 and verify shapes in Titanic dataset
# Drop non-numeric, redundant, or target columns to isolate features (X)
X = df[['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked']]
y = df['survived']

# Perform 80/20 train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Verify the matrix structures
print(f"X_train Shape: {X_train.shape} | X_test Shape: {X_test.shape}")
print(f"y_train Shape: {y_train.shape} | y_test Shape: {y_test.shape}")

print("----------------PROGRAM-5------------------")
#PROGRAM-5
#Create a correlation heatmap and identify top 5 features in Titanic dataset
df = sns.load_dataset("titanic")
df_mat = df[['survived' , 'pclass' , 'age' , 'sibsp' , 'fare']]
corr_matrix = df_mat.corr()
print(corr_matrix)
fig = plt.figure()
sns.heatmap(corr_matrix ,annot = True , cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
fig.savefig("P5Heatmap plot.png")
top_5_features = corr_matrix['survived'].abs().sort_values(ascending=False).index[0:6]
print("\nTop 5 features strongly correlated with Survival:\n", list(top_5_features))