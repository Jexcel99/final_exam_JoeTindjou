# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Import necessary libraries
import pandas as pd  # For handling data tables
import matplotlib.pyplot as plt  # For basic plotting
import seaborn as sns  # For advanced data visualizations

# Set default Seaborn style for all plots
sns.set(style='whitegrid')

# Load the CSV file 
df = pd.read_csv("/Users/joe/Desktop/TINDJOU Joe - bank_loans.csv")  # Read the dataset into a pandas DataFrame


# Step 1: Basic Data Inspection


print("Data types:")
print(df.dtypes)  # Display the data type of each column

print("\nMissing values per column:")
print(df.isnull().sum())  # Show the number of missing values per column

print("\nSummary statistics:")
print(df.describe())  # Show statistical summary for numeric columns

df.drop_duplicates(inplace=True)  # Remove any duplicated rows from the dataset


#  Visualization 1 - Loan Amount Distribution


plt.figure(figsize=(8, 5))  # Set plot size
sns.histplot(df['Loan Amount'], bins=30, kde=True)  # Plot histogram with KDE line
plt.title("Distribution of Loan Amounts")  # Add title to the plot
plt.xlabel("Loan Amount")  # Label for X-axis
plt.ylabel("Frequency")  # Label for Y-axis
plt.tight_layout()  # Adjust spacing to avoid label cut-off
plt.show()  # Display the plot


#  Visualization 2 - Loan Grade Distribution

plt.figure(figsize=(7, 5))  # Set figure size
sns.countplot(data=df, x='Grade', order=sorted(df['Grade'].unique()))  # Count how many loans are in each grade
plt.title("Loan Grade Distribution")  # Set chart title
plt.xlabel("Grade")  # Label X-axis
plt.ylabel("Number of Loans")  # Label Y-axis
plt.tight_layout()  # Optimize spacing
plt.show()  # Show the plot


#  Visualization 3 - Interest Rate by Grade


plt.figure(figsize=(8, 5))  # Set chart size
sns.boxplot(data=df, x='Grade', y='Interest Rate', order=sorted(df['Grade'].unique()))  # Boxplot of interest rate by grade
plt.title("Interest Rate by Loan Grade")  # Add chart title
plt.xlabel("Grade")  # Label for X-axis
plt.ylabel("Interest Rate (%)")  # Label for Y-axis
plt.tight_layout()  # Optimize layout
plt.show()  # Show the visualization


#  Visualization 4 - Funded Amount vs Loan Amount


plt.figure(figsize=(8, 5))  # Set figure size
sns.scatterplot(data=df, x='Loan Amount', y='Funded Amount', alpha=0.5)  # Scatterplot to compare amounts
plt.title("Funded Amount vs Loan Amount")  # Add title
plt.xlabel("Loan Amount")  # X-axis label
plt.ylabel("Funded Amount")  # Y-axis label
plt.tight_layout()  # Adjust spacing
plt.show()  # Display the plot


# Visualization 5 - Interest Rate by Employment Duration

plt.figure(figsize=(10, 5))  # Define figure size
sns.boxplot(data=df, x='Employment Duration', y='Interest Rate')  # Boxplot of interest rate by employment status
plt.title("Interest Rate by Employment Duration")  # Title of the graph
plt.xlabel("Employment Duration")  # Label for the x-axis
plt.ylabel("Interest Rate (%)")  # Label for the y-axis
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.tight_layout()  # Adjust layout to fit everything
plt.show()  # Show the final chart






