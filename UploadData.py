# -*- coding: utf-8 -*-
# upload.py
# automate filling in web forms(Kriss)

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import time
import os

url = "https://www.station.re.kr/group/kriss-materials-data-center/data-management"

options = webdriver.ChromeOptions()
driver = webdriver.Chrome('Data/chromedriver')

driver.get(url)

# login process
driver.find_element_by_id('_com_liferay_login_web_portlet_LoginPortlet_login').send_keys('ki0086')
driver.find_element_by_id('_com_liferay_login_web_portlet_LoginPortlet_password').send_keys('evoid8913')
driver.find_element_by_css_selector('button.gradient-btn.col-md-12.h-100.border-0').click()

# after login, switch to iframe
# there are two iframes(1. file_tree / 2. data info edit )

time.sleep(10)
iframes = driver.find_elements_by_tag_name('iframe')

# 1. processing file_tree iframe
tree_iframe = iframes[0]
driver.switch_to.frame(tree_iframe)

# expanding the tree
tree = 'fancytree-node fancytree-folder fancytree-lastsib fancytree-exp-nl fancytree-ico-cf'
tree_element = driver.find_element_by_xpath('//*[@id="ft-id-1"]/li/span')
webdriver.ActionChains(driver).move_to_element(tree_element).click(tree_element).perform()

# 3 type of function ( image / QA / text )
# step :
# 1. down to under the tree -> 2.Entry add -> 3. fill requirements : meta data, file

# < Image >
# 1.device_data_1.0.0
# 2.endurance_data_1.0.0
# 3.IV_curve_1.0.0
# 4. retention_data_1.0.0

time.sleep(10)
image_element = driver.find_element_by_xpath('//*[@id="ui-id-1"]/ul/li[1]/span/span[2]')
webdriver.ActionChains(driver).move_to_element(image_element).click(image_element).perform()

time.sleep(10)
image_element_2 = driver.find_element_by_xpath('//*[@id="ui-id-2"]/ul/li[1]/span/span[2]')
webdriver.ActionChains(driver).move_to_element(image_element_2).click(image_element_2).perform()

# Entry Button 누르기
# go to default iframe -> entry iframe -> click entry botton
driver.switch_to.default_content()

info_frame = driver.find_element_by_id('_OSPVisualizing_analyzer_DataInfo_INSTANCE_LAYOUT_canvas')
driver.switch_to.frame(info_frame)
print('enter info_frame')

# hit the button
# button tag 2개고, id값 새로고침 할 때마다 바뀜 (Xpath, id값 절대 쓰면 X)
time.sleep(10)
entry_button = driver.find_element_by_class_name('button-holder dialog-footer w-100')
print(entry_button)
ActionChains(driver).move_to_element(entry_button).click(entry_button).perform()
print('click entry button')

# file 선택
time.sleep(10)
driver.find_element_by_id("_OSPVisualizing_analyzer_DataInfo_dataFile").send_keys(os.getcwd()+"/Data/word.csv")

# method for refreshing to the tree iframe
def refresh_to_tree(tree_iframe, tree_element):
    driver.switch_to.default_content()
    driver.switch_to.frame(tree_iframe)
    webdriver.ActionChains(driver).move_to_element(tree_element).click(tree_element).perform()


# element = wait.until(EC.element_to_be_clickable((By.XPATH, root)))
# element.click()
# element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, tree))).click()
# //*[@id="ui-id-1"]/ul/li[1]/span/span[2]

# def imageUpload():

# QA_sheet_1.0.0/QA_data_1.0.0
# def QA():

# 1.paragraph_labeling_1.0.0
# 2.text_labeling_1.0.0
# def textUpload():


