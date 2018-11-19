
#### ATTENTION: In order to run with Chrome, need to download the drive. It is available at: http://chromedriver.chromium.org/downloads

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
# htmlGetJob= browser.find_element_by_id('sja2').click()

# get link element
link = browser.find_element_by_id('sja2')
# copy link address
link_address = link.get_attribute("href")

# go to link
browser.get(link_address)

#Pop up second page , ERRROR here
# htmlApplyJob=browser.find_element_by_id('vjs-container') #id="vjs-container" is container of second page
# htmlApplyJob=browser.find_element_by_class_name('indeed-apply-button').click()# <a href> ,Apply button on second page 

# second page now loaded in current browser

# get job title
job_title = browser.find_element_by_class_name("jobsearch-JobInfoHeader-title").text
salary = browser.find_element_by_class_name("jobsearch-JobMetadataHeader-item").text
#... more stuff :)

print("Job title: ", job_title)
print("salary: ", salary)
