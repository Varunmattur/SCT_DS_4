import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
path_to_file = "C:/Users/YourUsername/Desktop/SCT_DS_4/accidents.csv"  # Update with your actual path
data = pd.read_csv(path_to_file)

# Data preprocessing
data.dropna(inplace=True)  # Handling missing values (simple approach)

# Convert time column to datetime if applicable
if 'time_column' in data.columns:  # Replace 'time_column' with actual column name
    data['time_column'] = pd.to_datetime(data['time_column'])

# Analysis - example: accident counts by weather condition
accident_by_weather = data['weather_condition'].value_counts()

# Visualization - example: bar plot for accidents by weather condition
plt.figure(figsize=(10, 6))
sns.barplot(x=accident_by_weather.index, y=accident_by_weather.values)
plt.title('Accidents by Weather Condition')
plt.xlabel('Weather Condition')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()
