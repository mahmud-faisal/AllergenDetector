import pandas as pd
import os

# Assuming the CSV file is located in the "Data" directory next to your script
file_path = os.path.join(os.path.dirname(__file__), "Data", "food_ingredients_and_allergens.csv")

# Read the CSV file into a DataFrame
data = pd.read_csv(file_path)

print(data)

y = data['Prediction']
x= data.drop('Prediction',axis=1)
print(x)