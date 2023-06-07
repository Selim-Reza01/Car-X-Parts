#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Image Collecting and Renaming Script
import os
import shutil
import pandas as pd

# Load the data from Excel
df = pd.read_excel('D:\\scripts\\toyota\\toyota_input.xlsx')

# Split the 'id' column into make, model, and year
df[['make', 'model', 'year']] = df['id'].str.split('_', expand=True)

# Convert 'year' column to numeric
df['year'] = pd.to_numeric(df['year'], errors='coerce')

# Sort the DataFrame by 'model' and 'year' in ascending order
df.sort_values(['model', 'year'], inplace=True)

# Forward fill the missing values in the 'image' column within each group of 'model'
df['image'] = df.groupby('model')['image'].fillna(method='ffill')

# Backward fill the missing values in the 'image' column within each group of 'model'
df['image'] = df.groupby('model')['image'].fillna(method='bfill')

# Convert the 'year' column back to string
df['year'] = df['year'].astype(str)

# Save the updated DataFrame back to the Excel file
df.to_excel('D:\\scripts\\toyota\\toyota_input.xlsx', index=False)

# Input and output folders
image_folder = "D:\\scripts\\toyota\\car_images"
output_folder = "D:\\scripts\\toyota\\output-images"

# Read the data from the updated Excel sheet
df = pd.read_excel('D:\\scripts\\toyota\\toyota_input.xlsx')

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    image_name = row['image']
    
    # Check if image name exists
    if pd.notnull(image_name):
        image_path = os.path.join(image_folder, image_name)
        
        # Check if image file exists in the car-images folder
        if os.path.isfile(image_path):
            # Generate the new image name
            new_image_name = f"{row['id']}.jpg"
            new_image_path = os.path.join(output_folder, new_image_name)
            
            # Copy and rename the image file
            shutil.copy(image_path, new_image_path)
            
            print(f"Image '{image_name}' copied and renamed as '{new_image_name}'")
        else:
            print(f"Image '{image_name}' not found in the car-images folder")
    else:
        print(f"No image name provided for ID '{row['id']}'")

print("Image copying and renaming complete.")

