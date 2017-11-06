from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Safari()

browser.get('https://servicos.ulbra.br/ALEPH')

browser.find_element_by_xpath('//a[contains(text(), " Usuário / Renovação")]').click()

browser.find_element_by_name('bor_id').send_keys('110963010')

browser.find_element_by_xpath('//alt[contains(text(), " Identificação")]').click()