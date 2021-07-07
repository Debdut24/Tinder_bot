# Tinder bot made using Python and selenium webdriver to automate Tinder. The application logs in to the Tinder account and swipes right swipes until the list ends.(NB: Throughout the program xpath of links have been used which are updated from time to time in the website. Regular updates are to be made in the application for the proper functioning of the application.
import selenium.common.exceptions
from selenium import webdriver
import os
import time

phone_no = os.environ.get("PHONE_NO")
password = os.environ.get("PASSWORD")

driver_path = "D:/chromedriver.exe"
driver = webdriver.Chrome(executable_path = driver_path)
driver.get("https://www.tinder.com")
log_in = driver.find_element_by_link_text("LOG IN")
log_in.click()
time.sleep(5)
try:
    fb_login = driver.find_element_by_xpath ('//*[@id="q-1813346480"]/div/div/div[1]/div/div[3]/span/div[2]/button')
#   Note 1:update the xpath for the proper functioning
except selenium.common.exceptions.NoSuchElementException:
    more_option = driver.find_element_by_xpath('//*[@id="q-1813346480"]/div/div/div[1]/div/div[3]/span/button')
    #Note 1:
    more_option.click()
    time.sleep(3)
    fb_login = driver.find_element_by_xpath ('//*[@id="q-1813346480"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    #Note 1:
    fb_login.click()
else:
    fb_login.click()

time.sleep(5)
window = driver.window_handles
driver.switch_to.window(window[1])

email_entry = driver.find_element_by_xpath('//*[@id="email"]')
email_entry.send_keys(phone_no)
password_entry = driver.find_element_by_xpath('//*[@id="pass"]')
password_entry.send_keys(password)
login_button = driver.find_element_by_xpath('//*[@id="loginbutton"]')
login_button.click()
driver.switch_to.window(window[0])
time.sleep(5)
#Note 1:
allow_button = driver.find_element_by_xpath('//*[@id="q-1813346480"]/div/div/div/div/div[3]/button[1]')

allow_button.click()
time.sleep(3)
#Note 1:
notification_button = driver.find_element_by_xpath('//*[@id="q-1813346480"]/div/div/div/div/div[3]/button[1]')
notification_button.click()
time.sleep(10)
#Note 1:
like_button = driver.find_element_by_xpath('//*[@id="q-84965404"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
for n in range(0,50):
    like_button.click()
    driver.execute_script ("arguments[0].click();", like_button)
    time.sleep(2)
