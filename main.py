from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("C:/Users/Daniyal/OneDrive/Desktop/C-127/c127-Web-scrapping-1-main/chromedriver.exe")

scraped_data = []

def scrape():
 
 
 
    soup = BeautifulSoup(browser.page_source, "html.parser")
    bright_star_table = soup.find("table", attrs={"class","wikitable"})
    table_body = bright_star_table.find('tbody')
    table_rows = table_body.find_all('tr')
    temp_list=[]

    for row in table_rows:
        table_cols = row.find_all('td')
        print(table_cols)
        for col_data in table_cols:
            print(col_data.text)
            data = col_data.text.strip()
            print(data)

            temp_list.append(data)
    scraped_data.append(temp_list)





    
# Calling Method    
scrape()