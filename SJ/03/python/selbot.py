# /Users/hyeonseongjun/Desktop/mypro/chromedriver

from urlparse import urlparse
from selenium import webdriver


driver = webdriver.Chrome('/Users/hyeonseongjun/Desktop/mypro/chromedriver')
driver.implicitly_wait(3)

if 