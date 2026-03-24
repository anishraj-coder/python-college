import pandas as pd

df = pd.read_csv("D:\\Anish_DMV_Lab\\salary_dataset.csv")

print("--- Missing Values Before ---")
print(df.isnull().sum())

df = df.fillna(df.mean(numeric_only=True))

print("\n--- Cleaned Data ---")
print(df.to_string())

