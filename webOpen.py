
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
# link = browser.find_element_by_id('sja1')

# get all jobs in current page
links = browser.find_elements_by_class_name('jobtitle')
link_ids = []

for index in range(len(links)):
    link = links[index]
    link_ids.append(link.get_attribute('id'))

for index in range(len(link_ids)):
    # copy link address
    link_id = link_ids[index]
    link = browser.find_element_by_id(link_id)
    link_address = link.get_attribute("href")

    # go to link
    browser.get(link_address)

    # get job info
    job_title = browser.find_element_by_class_name("jobsearch-JobInfoHeader-title").text
    # salary = browser.find_element_by_class_name("jobsearch-JobMetadataHeader-item").text

    print("Job title: ", job_title)

    #apply= browser.find_element_by_id("indeedApplyButtonContainer").click()
    apply= browser.find_element_by_class_name("jobsearch-IndeedApplyButton")
    apply.click()

    ### DO STUFF HERE TO APPLY FOR CURRENT JOB IN LOOP ###

    #===========iFrame=========================================
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
    upload_element = browser.find_element_by_class_name("ia-BrowserDefaultFilePicker-control")
    # upload_element.click()
    upload_element.send_keys("C:/resume_sample.pdf")

    ### AFTER APPLYING FOR THIC CURRENT JOB, GO BACK TO JOB LIST 
    ### TO MAKE SURE NEXT LINK IS OBTAINED

    browser.execute_script("window.history.go(-1)")     # back one to get out of iframe
    browser.execute_script("window.history.go(-1)")     # back one to get back to page list

#=========================================================

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
