
#### ATTENTION: In order to run with Chrome, need to download the drive. It is available at: http://chromedriver.chromium.org/downloads

#import webbrowser
#wb=webbrowser.open("www.google.com")

from  selenium import webdriver
from  selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://ca.indeed.com")
#
#enter the job titlt
htmlSearch= browser.find_element_by_id('text-input-what')
htmlSearch.send_keys("junior developer")
htmlSearch.send_keys(Keys.ENTER)

# get link element
link = browser.find_element_by_id('sja1')
# copy link address
link_address = link.get_attribute("href")

# go to link
browser.get(link_address)

# second page now loaded in current browser
# get job title
job_title = browser.find_element_by_class_name("jobsearch-JobInfoHeader-title").text
#salary = browser.find_element_by_class_name("jobsearch-JobMetadataHeader-item").text

#apply= browser.find_element_by_id("indeedApplyButtonContainer").click()
apply= browser.find_element_by_class_name("jobsearch-IndeedApplyButton")
apply.click()

#time.sleep(15)
#print("test", browser.find_element_by_class_name("indeed-apply-bd"))
# netmail

# get the list of iframes present on the web page using tag "iframe"
iframe = browser.find_elements_by_tag_name("iframe")

# Switch to the frame[0]
print("frame0 ",browser.switch_to_frame(iframe[0]))

# Need to go back to default content if want to go to ANOTHER FRAME,IF only 1 frame , do not need to  switch_to_default_content
#browser.switch_to_default_content()

#print("frame1 ",browser.switch_to_frame(iframe[1]))
# go to "Second" iframe to look for src then open it to new browser
src= browser.find_element_by_tag_name("iframe").get_attribute("src")
getSrc= browser.get(src)
browser.find_element_by_class_name("ia-BrowserDefaultFilePicker-control").click()

print("No of frames present in the web page are: ", len(iframe))

"""#switching between the iframes based on index
for index in range(len(seq)):
    browser.switch_to_default_content()
    iframe = browser.find_elements_by_tag_name('iframe')[index]
    browser.switch_to.frame(iframe)
    browser.implicitly_wait(30)

    #highlight the contents of the selected iframe

    browser.find_element_by_tag_name('a').send_keys(Keys.CONTROL, 'a')
    time.sleep(2)
"""
 

print("Job title: ", job_title)
print("apply: ", apply)