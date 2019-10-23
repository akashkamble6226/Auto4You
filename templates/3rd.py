import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('C:/Users/AKASH/PycharmProjects/plot/national.csv')

print(df.head())

x = df['period']
y = df['population']

plt.bar(x, y,color='g')
plt.xlabel('period')
plt.ylabel('Increasing population')
plt.title('Migrations & Populations')
plt.show()



country_data = df["period"]
medal_data = df["population"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
explode = (1, 0, 0, 0, 0)  
plt.pie(medal_data, labels=country_data, explode=explode, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Migrations&Populations")
plt.show()