# Create a correlation heatmap and identify top 5 features in Titanic dataset

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = sns.load_dataset("titanic")
df_mat = df[['survived' , 'pclass' , 'age' , 'sibsp' , 'fare']]
corr_matrix = df_mat.corr()
print(corr_matrix)
fig = plt.figure()
sns.heatmap(corr_matrix)
plt.title('Correlation Heatmap')
plt.show()
fig.savefig("Heatmap plot.png")
top_5_features = corr_matrix['survived'].abs().sort_values(ascending=False).index[0:6]
print("\nTop 5 features strongly correlated with Survival:\n", list(top_5_features))
