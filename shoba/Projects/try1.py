
import sys
import selenium
from selenium import webdriver
br = webdriver.Firefox()
br.get("https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/")
br.implicitly_wait(30)
br.close()