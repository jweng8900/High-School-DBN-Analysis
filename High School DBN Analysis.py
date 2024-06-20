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

# Define the School DBN letters to filter
school_dbn_letters = ['M', 'X', 'Q', 'K']

# Initialize empty lists for storing results
result_data = []

# Loop through each school DBN letter and calculate mean scores
for letter in school_dbn_letters:
    contains_letter_df = filtered_df[filtered_df['School DBN'].str.contains(letter)]
    mean_scores = contains_letter_df.groupby('School DBN')['Mean Score'].mean().reset_index()
    average_mean_score = mean_scores['Mean Score'].mean()
    result_data.append({'School DBN': f'{letter} School DBNs', 'Average Mean Score': average_mean_score})

# Create DataFrame from result_data
plot_df = pd.DataFrame(result_data)

# Calculate the overall average mean score
overall_average = plot_df['Average Mean Score'].mean()

# Plotting the results
plt.figure(figsize=(12, 6))

plt.bar(plot_df['School DBN'], plot_df['Average Mean Score'], color=['blue', 'orange', 'green', 'red'], alpha=0.7)

# Plot the overall average as a horizontal line
plt.axhline(y=overall_average, color='gray', linestyle='--', label=f'Overall Average: {overall_average:.2f}')

plt.xlabel('School DBN')
plt.ylabel('Average Mean Score')
plt.title('Comparison of Average Mean Scores for School DBNs Containing "M", "X", "Q", and "K"')
plt.xticks(rotation=0)  # Rotate x-axis labels if needed
plt.legend()

plt.tight_layout()
plt.show()