# To make this app work there must be a 'dummy' mail account made, otherwise, gmail itself will block the web 
# driver interaction by impliying that the procedure is not secure

# There's another way to make this automation without the usage of a new account
# It requires the usage of another library called seleniumwire

# To begin this bot app its required to download the webdriver for any browser we may want to work with
# And set it up accordingly. 

# In this case I'll be using Google Chrome and Firefox for which I had to add the path of the web driver to the enviromnet 
# variable path and reboot the PC before executing this script

# The safety feature taht prevents Gmail to be accessed by a bot can be bypassed by:
# 1 - Login in to Gmail
# 2 - Accessing to the link bellow 
# https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4MmOPP_ZAOaIp-wL6A0TanrVQc7gEN1Bc5cekNWSR6b2vBzA1z-DaKyJdxYfra9lmv4N75KbQgMepcZ3qUhEgKEZiuRIw
# 3 - Allowing acces to not safe apps

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
from config import mail,password

tag_id = 'identifierId'
next_button = 'VfPpkd-vQzf8d'

url = 'http://gmail.com'

browser = webdriver.Chrome()

# options = Options()
# options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
# # There must be setted up this instructio so Selenium can access the Firefox executable
# browser = webdriver.Firefox(options=options)
print ('browser = ',browser)
print ('type(browser) = ',type(browser))
# This instruction createss an instance that open the browser
# Here is where is decided which browser can be used. 'Chrome()' can be
# changed by Firefox or any other availabe browser
# This is a <class 'selenium.webdriver.chrome.webdriver.WebDriver'> object

browser.get(url)
# The 'get()' Method recieves a string with an URL to access

username_field = browser.find_element_by_id(tag_id)
print ('username_field = ',username_field)
print ('type(username_field) = ',type(username_field))
# The 'find_element_by_id()' method reviews the HTML file to find a perticular ID of a tag
# This instruction returns a object <class 'selenium.webdriver.remote.webelement.WebElement'> type

username_field.send_keys(mail)
# It 'send_keys()' recieves data (in this case in the form of a string) and send it to a particular
# Field in the website

next_btn = browser.find_element_by_class_name(next_button)
# The 'find_element_by_class_name()' method reviews the HTML file to find a perticular Class of a tag
print ('next_btn = ',next_btn)
print ('type(next_btn) = ',type(next_btn))
# This instruction return a object <class 'selenium.webdriver.remote.webelement.WebElement'>
next_btn.click()

time.sleep (20)
# There will be a time where we'll wait for the Gmail's animation occurs

# Note: This method is no longer available, at least under the instructions offered in the UDEMY 
# course, any way, the process will be documented

# Once the password field appears, the field will be found by the XPath (for more information about this element go to
# "\study\python\ad_notes\xml\notes.txt" The last topic is reated to the XPath of XML)

password_field = browser.find_element(by = By.XPATH, value = '//*[@id="password"]/div[1]/div/div[1]/input')
print ('password_field = ',password_field)
print ('type(password_field) = ',type(password_field))
# The Xpath of the password fiel is located

password_field.send_keys(password)
# THis instruction will input the password on the password field

next_btn.click()
# THis instruction will click on the next button