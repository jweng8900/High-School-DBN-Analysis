import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('https://raw.githubusercontent.com/CunyLaguardiaDataAnalytics/datasets/master/2014-15_To_2016-17_School-_Level_NYC_Regents_Report_For_All_Variables.csv')

# Filter the DataFrame to include only 'High school' in 'School Level'
high_school_df = df[df['School Level'] == 'High school']

# Convert 'Mean Score' to numeric and filter out non-numeric values
high_school_df['Mean Score'] = pd.to_numeric(high_school_df['Mean Score'], errors='coerce')
filtered_df = high_school_df[high_school_df['Mean Score'].notnull()]

# Define columns to drop
dropped_cols = [
    'Number Scoring Below 65', 'Percent Scoring Below 65',
    'Number Scoring 65 or Above', 'Percent Scoring 65 or Above',
    'Number Scoring 80 or Above', 'Percent Scoring 80 or Above',
    'Number Scoring CR', 'Percent Scoring CR'
]

# Drop specified columns
filtered_df = filtered_df.drop(dropped_cols, axis=1)

# Drop rows with any NaN values
filtered_df = filtered_df.dropna()

# Filter rows where 'School DBN' contains 'M'
contains_m_df = filtered_df[filtered_df['School DBN'].str.contains('M')]

# Group by 'School DBN' and calculate the mean of 'Mean Score' for 'M'
m_result = contains_m_df.groupby('School DBN')['Mean Score'].mean().reset_index()

# Filter rows where 'School DBN' contains 'X'
contains_x_df = filtered_df[filtered_df['School DBN'].str.contains('X')]

# Group by 'School DBN' and calculate the mean of 'Mean Score' for 'X'
x_result = contains_x_df.groupby('School DBN')['Mean Score'].mean().reset_index()

# Filter rows where 'School DBN' contains 'Q'
contains_q_df = filtered_df[filtered_df['School DBN'].str.contains('Q')]

# Group by 'School DBN' and calculate the mean of 'Mean Score' for 'Q'
q_result = contains_q_df.groupby('School DBN')['Mean Score'].mean().reset_index()

# Filter rows where 'School DBN' contains 'K'
contains_k_df = filtered_df[filtered_df['School DBN'].str.contains('K')]

# Group by 'School DBN' and calculate the mean of 'Mean Score' for 'K'
k_result = contains_k_df.groupby('School DBN')['Mean Score'].mean().reset_index()

# Plotting the results
plt.figure(figsize=(16, 8))

# Plot for 'M' results
plt.bar(m_result['School DBN'], m_result['Mean Score'], alpha=0.6, label='M School DBNs')

# Plot for 'X' results
plt.bar(x_result['School DBN'], x_result['Mean Score'], alpha=0.6, label='X School DBNs')

# Plot for 'Q' results
plt.bar(q_result['School DBN'], q_result['Mean Score'], alpha=0.6, label='Q School DBNs')

# Plot for 'K' results
plt.bar(k_result['School DBN'], k_result['Mean Score'], alpha=0.6, label='K School DBNs')

plt.xlabel('School DBN')
plt.ylabel('Mean Score')
plt.title('Comparison of Mean Scores for School DBNs Containing "M", "X", "Q", and "K"')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.legend()

plt.tight_layout()
plt.show()

average_m = m_result['Mean Score'].mean()
average_x = x_result['Mean Score'].mean()
average_q = q_result['Mean Score'].mean()
average_k = k_result['Mean Score'].mean()

# Prepare data for plotting
data = {
    'School DBN': ['M School DBNs', 'X School DBNs','Q School DBNs','K School DBNs'],
    'Average Mean Score': [average_m, average_x,average_q, average_k]
}
plot_df = pd.DataFrame(data)

# Plotting the results
plt.figure(figsize=(10, 6))

plt.bar(plot_df['School DBN'], plot_df['Average Mean Score'], color=['blue', 'orange','yellow','purple'], alpha=0.7)

plt.xlabel('School DBN')
plt.ylabel('Average Mean Score')
plt.title('Comparison of Average Mean Scores for School DBNs Containing "M" and "X"')

plt.show()