#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import shutil
import pandas as pd

# Define the folder
folder_path = '/content/drive/MyDrive/all_images/555'

# Define the subfolder
subfolders = ['images', 'images_using_placeholder', 'placeholder']

# Define the Excel file
excel_file = '/content/drive/MyDrive/all_images/555/part_number.xlsx'

# Read the Excel file
df = pd.read_excel(os.path.join(folder_path, excel_file))

# Get the list of image files in the images folder
image_files = os.listdir(os.path.join(folder_path, 'images'))

# Extract part numbers from image file names
existing_part_numbers = set([filename.split('_')[2] for filename in image_files])

# Iterate over the rows in the Excel file
for _, row in df.iterrows():
    # Extract the values from the row
    brand, product_name, part_number, image_number = row[0].split('_')

    # Check if the part number is absent in the images folder
    if part_number not in existing_part_numbers:
        # Get the path of the placeholder image
        placeholder_image_path = os.path.join(folder_path, 'placeholder', f'{brand}_{product_name}.jpg')

        # Create the new file name for the image using the part number
        new_image_name = f'{brand}_{product_name}_{part_number}_1.jpg'

        # Get the destination path for the new image
        destination_path = os.path.join(folder_path, 'images_using_placeholder', new_image_name)

        # Copy the placeholder image to the destination path
        shutil.copy(placeholder_image_path, destination_path)

        # Print the details of the copied image
        print(f'Copied image: {new_image_name}')

print('Image copying complete.')

