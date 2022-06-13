from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

id_product = 'MD506Z/A'
search_form_path = "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/div/form/div/div/input"
search_button_path = "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/div/form/button"
buy_button_path = "/html/body/app-root/div/div/rz-product/div/product-tab-main/div[1]/div[1]/div[2]/rz-product-main-info/div[2]/div/ul/li[1]/app-product-buy-btn/app-buy-button/button"
close_button_path = "/html/body/app-root/single-modal-window/div[3]/div[1]/button"
main_page_path = "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/a/picture/img"
basket_path = "/html/body/app-root/div/div/rz-main-page/div/main/main-page-content/app-small-cart/section/button[1]"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://rozetka.com.ua/")

SearchForm = driver.find_element(By.XPATH, search_form_path).send_keys(id_product)
SearchButton = driver.find_element(By.XPATH, search_button_path).click()
time.sleep(2)

BuyButton = driver.find_element(By.XPATH, buy_button_path).click()
time.sleep(5)

Close_Button = driver.find_element(By.XPATH, close_button_path).click()
time.sleep(5)

Main_page = driver.find_element(By.XPATH, main_page_path).click()
time.sleep(5)

basket = driver.find_element(By.XPATH, basket_path).click()
time.sleep(5)

driver.close()
driver.quit()

