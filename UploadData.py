# -*- coding: utf-8 -*-
# upload.py
# automate filling in web forms(Kriss)

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import time

url = "https://www.station.re.kr/group/kriss-materials-data-center/data-management"

options = webdriver.ChromeOptions()
driver = webdriver.Chrome('Data/chromedriver')

driver.get(url)

# login process
driver.find_element_by_id('_com_liferay_login_web_portlet_LoginPortlet_login').send_keys('ki0086')
driver.find_element_by_id('_com_liferay_login_web_portlet_LoginPortlet_password').send_keys('evoid8913')
driver.find_element_by_css_selector('button.gradient-btn.col-md-12.h-100.border-0').click()

# after login, switch to iframe
time.sleep(10)
iframe = driver.find_element_by_tag_name('iframe')
# iframe = driver.find_element_by_id(iframe_class)
driver.switch_to.frame(iframe)
print(iframe)
print("iframe")

# after login
root = '//[@id="ft-id-1"]/li/span'

element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, root))).click()
element.click()

# element = wait.until(EC.element_to_be_clickable((By.XPATH, root)))
print("wait")
# element.click()
print("y")

webdriver.ActionChains(driver).move_to_element(root).click(root).perform()


# 3 type of function ( image / QA / text )
# Entry add -> requirement : meta data, file

# Article_data_1.0.0/image_data_1.0.0
# 1.device_data_1.0.0
# 2.endurance_data_1.0.0
# 3.IV_curve_1.0.0
# 4. retention_data_1.0.0
# def imageUpload():

# QA_sheet_1.0.0/QA_data_1.0.0
# def QA():

# 1.paragraph_labeling_1.0.0
# 2.text_labeling_1.0.0
# def textUpload():


