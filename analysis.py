import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("sales.csv", encoding="latin1")

# Cleaning
df.drop_duplicates(inplace=True)
df["Sales"].fillna(df["Sales"].median(), inplace=True)
df["Profit"].fillna(df["Profit"].median(), inplace=True)
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Analysis
print(df.head())
print("\nShape:", df.shape)
print("\nStatistics:\n", df.describe())
print("\nMissing Values:\n", df.isnull().sum())

# 1. Bar Chart
df.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.savefig("graph1_bar.png")
plt.close()

# 2. Pie Chart
df.groupby("Region")["Sales"].sum().plot(
    kind="pie", autopct="%1.1f%%")
plt.title("Sales by Region")
plt.ylabel("")
plt.savefig("graph2_pie.png")
plt.close()

# 3. Line Chart
monthly = df.groupby(
    df["Order Date"].dt.to_period("M"))["Sales"].sum()
plt.plot(monthly.index.astype(str), monthly.values)
plt.title("Monthly Sales Trend")
plt.xticks(rotation=45)
plt.savefig("graph3_line.png")
plt.close()

# 4. Scatter Plot
sns.scatterplot(data=df, x="Sales", y="Profit")
plt.title("Sales vs Profit")
plt.savefig("graph4_scatter.png")
plt.close()

# 5. Histogram
plt.hist(df["Sales"], bins=20, edgecolor="black")
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.savefig("graph5_histogram.png")
plt.close()

# 6. Heatmap
sns.heatmap(
    df[["Sales","Profit","Quantity","Discount"]].corr(),
    annot=True)
plt.title("Correlation Heatmap")
plt.savefig("graph6_heatmap.png")
plt.close()

# Save cleaned data
df.to_csv("cleaned_sales.csv", index=False)

print("\nDONE! 6 graphs created successfully.")