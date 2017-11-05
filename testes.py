#coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Safari()

# NetAula
cgu = 'xxx'
password = 'xxx'
driver.get('https://servicos.ulbra.br/pls/ulbra24/AAMAIN.Login')

driver.find_element_by_id('i_Login').send_keys(cgu)
driver.find_element_by_name('i_Senha').send_keys(password)

driver.find_element_by_xpath('//a[contains(text(), "Conectar")]').click()

#links = driver.find_elements_by_xpath("//a[@href]")
#for links in links:
#    print (links.get_attribute("href"))

driver.quit