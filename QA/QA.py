from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("C:\\Users\Виктория\.wdm\drivers\chromedriver\win32\90.0.4430.24\chromedriver.exe")
browser.get("https://rezka.ag/")
time.sleep(3)
browser.find_element_by_id('search-field').send_keys("Lost")
time.sleep(3)
browser.find_element_by_id('search-field').send_keys(Keys.RETURN)
time.sleep(3)

txt = browser.find_element_by_css_selector('h1').text
assert txt.find("Lost") != -1  # ф-ция find() находит подстроку в строке, если нет - возвращает '-1' 

browser.find_element_by_link_text('Остаться в живых').click()
time.sleep(3)

txt = browser.find_element_by_class_name('b-post__title').text
assert txt.find("Остаться в живых") != -1
time.sleep(3)