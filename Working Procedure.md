Image Renaming Steps:

1. Get image in google drive

2. Rename with part number and image number

3. Download the image folder

4. Download part number, brand, product name for specific brand from database. Make sure all are in lowercase and every space replaced with '-'. Use this query: 
select distinct LOWER(part_number), LOWER(REPLACE(brand, ' ', '-')), LOWER(REPLACE(product_name, ' ', '-')) from parts where brand = '';

5. Change all image name into lowercase

6. Run Python Script for image renaming

7. Upload renamed image into google drive
