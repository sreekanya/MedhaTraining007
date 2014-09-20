#! /usr/bin/python 

import selenium 
from selenium import webdriver

wd=webdriver.Firefox()
wd.get("https://bing.com")
wd.close()

