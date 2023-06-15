#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

baseurl = 'http://www.sankei-555.com/search/'

product_links = []
page_limit = 524  # Specify the number of pages to retrieve

for x in range(1, page_limit + 1):
    y = (x - 1) * 20
    url = f'http://www.sankei-555.com/search/list.php?1=1&1=1&sch_mode=2&sch_pull_change=&p_id=10642&sch_p_maker2=&sch_p_car2=&sch_p_year2=&sch_p_hinmei2=&sch_p_maker=&sch_p_car=&sch_p_year=&sch_p_hinmei=&sch_p_555no=&sch_p_oemno=&offset={y}&page={x}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    div_contents = soup.find('div', id='contents')

    if div_contents:
        links = div_contents.find_all('a')
        for link in links:
            if 'detail.php?p_id=' in link.get('href', ''):
                product_link = baseurl + link['href']
                product_links.append(product_link)
    else:
        print(f"No contents found for page {x}")

print(len(product_links))

product_list = []
for links in product_links:
    r = requests.get(links)
    soup = BeautifulSoup(r.content, 'html.parser')

    data_table = soup.find('div', class_='data')
    rows = data_table.find_all('tr')

    part_number = rows[0].find('td').text.strip()
    make = rows[1].find('td').text.strip()
    model = rows[2].find('td').text.strip()
    year = rows[3].find('td').text.strip()
    chassis = rows[4].find('td').text.strip()
    location = rows[5].find('td').text.strip()

    noondata = {
        'Part_Number': part_number,
        'Make': make,
        'Model': model,
        'Year': year,
        'Chassis': chassis,
        'Location': location
    }

    product_list.append(noondata)
    print('Saving:', noondata['Part_Number'])

df = pd.DataFrame(product_list)

# Specify the folder path to save the Excel file
folder_path = 'D:\\scripts\\'

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Combine the folder path and file name to create the complete file path
file_path = os.path.join(folder_path, '555_Data(351-450).xlsx')

df.to_excel(file_path, index=False)
print('Task Completed Successfully!!')

