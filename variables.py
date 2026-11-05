
#%%
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\VS_Codes\Data Set\My\Titanic-Dataset.csv")
#%%
gender = df['Sex'].value_counts()
print(gender)
#%%
plt.bar(gender.index, gender.values)
plt.title("Passengers by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Passengers")
plt.show()
#%%

survival = df['Survived'].value_counts()

plt.pie(survival.values, labels=['Not Survived', 'Survived'],
        autopct='%1.1f%%')
plt.title("Titanic Survival Rate")
plt.show()

#%%
plt.hist(df['Age'].dropna(), bins=20, edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

#%%
age_count = df['Age'].value_counts().sort_index()

plt.plot(age_count.index, age_count.values, marker='o')
plt.title("Passenger Count by Age")
plt.xlabel("Age")
plt.ylabel("Passenger Count")
plt.show()

#%%
plt.scatter(df['Age'], df['Fare'])
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()
#%%

plt.boxplot(df['Fare'].dropna())
plt.title("Fare Distribution")
plt.ylabel("Fare")
plt.show()
# %%
