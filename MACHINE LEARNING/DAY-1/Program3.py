# Visualize feature distributions using Histograms and Pair Plots
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = sns.load_dataset("tips")
fig1 = plt.figure()
plt.subplot(1,2,1)
sns.histplot(df["total_bill"],kde=True)
plt.subplot(1,2,2)
sns.histplot(df['tip'],kde=True)
fig1.savefig("Histogram_plot.png")
plt.show()

fig2 = sns.pairplot(df,hue = 'sex')
fig2.savefig("Pair_plot.png")
plt.show()
