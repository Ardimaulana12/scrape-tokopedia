import time
import os
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.tokopedia.com/search?fcity=174%2C175%2C176%2C177%2C178%2C179&navsource=&ob=9&sc=3058&srp_component_id=04.06.00.00&srp_page_id=&srp_page_title=&st=&q=samsung')

nama_toko=None
lokasi=None
terjual=None
rate=None
data=[]
for i in range(2):
    WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".css-1asz3by")))
    time.sleep(2)
    for j in range(20):
        driver.execute_script('window.scrollBy(0,250)')
        time.sleep(1)
        
    driver.execute_script('window.scrollBy(50,0)')
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for item in soup.find_all('div', class_='css-1asz3by'):
        judul = item.find('div',class_='prd_link-product-name css-3um8ox').text
        harga = item.find('div',class_='prd_link-product-price css-h66vau').text
        for khusus_span in item.find_all('div',class_='css-1rn0irl'):
            lokasi = khusus_span.find('span',class_='prd_link-shop-loc css-1kdc32b flip').text
            nama_toko = khusus_span.find('span',class_='prd_link-shop-name css-1kdc32b flip').text
        for rating in item.find_all('div',class_='prd_shop-rating-average-and-label css-26zmlj'):
            terjual_element = rating.find('span',class_='prd_label-integrity css-1sgek4h')
            terjual = terjual_element.text if terjual_element else ""
            
            rate_element = rating.find('span',class_='prd_rating-average-text css-t70v7i')
            rate = rate_element.text if rate_element else ""
        data.append((judul,nama_toko,terjual,harga,rate,lokasi,))
    time.sleep(2)
    button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Laman berikutnya"]')
    driver.execute_script("arguments[0].click();", button)
    time.sleep(2)
df = pd.DataFrame(data,columns=('judul','nama_toko','terjual','harga','rate','lokasi'))
print(df)
df.to_excel("output_data_tes2.xlsx",index=False)
os.system("start output_data.xlsx")
    # Tunggu hingga lebih banyak konten dimuat
    # row = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.css-1asz3by")))
    # WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.css-rjanld > div > div > div > div > div > div > div > div > div > a > div.prd_link-product-name.css-3um8ox")))

    # Pilih semua elemen judul produk


    # Lakukan iterasi pada elemen-elemen judul dan cetak teksnya
    # for judul in row:
        # harga_elements = judul.find_element(By.CSS_SELECTOR, "div.css-1asz3by > a > div > div > div.prd_link-product-price.css-h66vau").text
        # judul_elements = judul.find_element(By.CSS_SELECTOR, "div.css-rjanld > div > div > div > div > div > div > div > div > div > a > div.prd_link-product-name.css-3um8ox").text
        # price_elements = judul.find_element(By.CSS_SELECTOR, "div.css-1asz3by > a > div > div > span.prd_label-integrity.css-1sgek4h").text
        # print(harga_elements)
    # driver.close()
