import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
data_path = '대전교통지수.xlsx'  # Make sure to update this path to your actual file location
df = pd.read_excel(data_path)


# Create a bar graph
plt.figure(figsize=(10, 6))
plt.bar(df['지역'], df['교통 지수'], color='skyblue')
plt.xlabel('Region', fontsize=12)
plt.ylabel('Transportation Index', fontsize=12)
plt.title('Transportation Index by Region in Daejeon', fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y')

# Show the plot
plt.tight_layout()
plt.show()