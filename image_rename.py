#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Image renaming by matching part_number

import os
import pandas as pd

# Load the excel file contains (part_number, brand, product_name)
excel_file = pd.read_excel('D:\\test\\part_number.xlsx')

# Create directories for renamed and unmatched images
renamed_dir = 'D:\\test\\renamed_images'
unmatched_dir = 'D:\\test\\unmatched_images'

# Create the directories if they don't exist
os.makedirs(renamed_dir,exist_ok=True)
os.makedirs(unmatched_dir,exist_ok=True)

# Loop through each image file
for filename in os.listdir('D:\\test\\images'):
    if filename.endswith('.jpg'):
        
        # Extract image id and image number
        part_number, image_number = filename.split('_')
        part_number = part_number.strip()
        image_number = image_number.replace('.jpg', '').strip()
        
        # Find matching row in Excel file
        row = excel_file.loc[excel_file['part_number'] == part_number]
        
       # If there's a match, rename the image and move it to the renamed directory
        if not row.empty:
            brand = row.iloc[0]['brand']
            product_name = row.iloc[0]['product_name']
            new_filename = f"{brand}_{product_name}_{part_number}_{image_number}.jpg"
            os.rename(os.path.join('D:\\test\\images', filename), os.path.join('D:\\test\\renamed_images', new_filename))
        else:
            # If there's no match, move the image to the unmatched directory
            os.rename(os.path.join('D:\\test\\images', filename), os.path.join('D:\\test\\unmatched_images',filename))

