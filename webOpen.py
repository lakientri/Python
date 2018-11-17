# this is testing
#import webbrowser
#wb=webbrowser.open("www.google.com")

from  selenium import webdriver
from  selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://ca.indeed.com/?r=us")

#enter the job titlt
htmlSearch= browser.find_element_by_id('text-input-what')
htmlSearch.send_keys("junior developer")
htmlSearch.send_keys(Keys.ENTER)

#choose the job title
htmlGetJob= browser.find_element_by_id('sja2').click()

#Pop up second page , ERRROR here
htmlApplyJob=browser.find_element_by_id('vjs-container') #id="vjs-container" is container of second page
htmlApplyJob=browser.find_element_by_class_name('indeed-apply-button').click()# <a href> ,Apply button on second page 


