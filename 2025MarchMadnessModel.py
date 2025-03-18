import pandas as pd

print("Setup successful! Pandas version:", pd.__version__)


df = pd.read_csv("Data/INT_KenPom_Defense.csv")
print(df.head())