from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
import time
import os
import datetime
from webdriver_manager.chrome import ChromeDriverManager

s1 = "https://www.amazon.in/s?k=philips+hair+straightener+brush&crid=L001OY4A89O4&sprefix=philips+hair+s%2Caps%2C288&ref=nb_sb_ss_i_2_14"
s2 = "https://www.flipkart.com/search?q=philips+hair+straightener&sid=zlw%2C79s%2Cdk5&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_na&as-pos=1&as-type=RECENT&suggestionId=philips+hair+straightener%7CHair+Straighteners&requestId=5cf5def2-cd3b-4593-aaef-472800192c09&as-backfill=on"
s3 = "https://www.snapdeal.com/search?keyword=philip%20hair%20straightener&santizedKeyword=sling+bag&catId=0&categoryId=0&suggested=true&vertical=p&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=ALL&url=&utmContent=&dealDetail=&sort=rlvncy"

wait_imp = 10
CO = webdriver.ChromeOptions()
CO.add_experimental_option('useAutomationExtension', False)
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-maximized')
wd = webdriver.Chrome(r'C:\Users\manas\chrome driver\chromedriver.exe', options=CO)

print("Your Bot is ready to scrape the info you need ..... \n")

print("Connecting to Amazon")
print("Fetching hair straightner info..")
wd.get(s1)
wd.implicitly_wait(wait_imp)
a = wd.find_element_by_xpath(
    "/html/body/div[1]/div[2]/div[1]/div/div[1]/div/span[3]/div[2]/div[6]/div/span/div/div/div[4]/div[1]/div/a/span[1]/span[2]/span[2]")
a_price = a.text
print("Price on amazon is \n")
print(a_price)
time.sleep(2)

print("Connecting to Flipkart")
print("Fetching hair straightner info..")
wd.get(s2)
wd.implicitly_wait(wait_imp)
b = wd.find_element_by_xpath(
    "/html/body/div/div/div[3]/div[2]/div[1]/div[2]/div[4]/div/div[2]/div/a[3]/div/div[1]")
b_price = b.text
print("Price on Flipkart is \n")
print(b_price)
time.sleep(2)

print("Connecting to snapdeal")
print("Fetching hair straightner info..")
wd.get(s3)
wd.implicitly_wait(wait_imp)
c = wd.find_element_by_id(
    "display-price-623373032776")
c_price = c.text
print(" price on snapdeal is\n")
print(c_price)
time.sleep(2)

