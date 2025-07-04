import pandas as pd

# Simple dummy data
data = {
    'Name': ['Ankush', 'Gopi', 'Mansi', 'Priya'],
    'Experience': [3, 5, 2, 4],
    'PerformanceScore': [87, 90, 70, 90],
    'Department': ['Engineering', 'Engineering', 'HR', 'Marketing'],
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('data/employees.csv', index=False)