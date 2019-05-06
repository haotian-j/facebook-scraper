from selenium import webdriver
from selenium.webdriver.common.by import By

#open firefox browser and navigate to page
driver = webdriver.Firefox()
driver.get("https://mobile.facebook.com/")

#login function
def fb_login():
    driver.get("https://mobile.facebook.com/")
    driver.find_element_by_id("m_login_email").send_keys("haotianj2000@gmail.com")
    driver.find_element_by_name("pass").send_keys("Jht207067!")
    driver.find_element_by_name("login").click()

#navigate to page
def page_nav(pageName):
    driver.find_element_by_class_name("bm.bo.bp.bq.bs.bn").click()
    driver.find_element_by_link_text("Menu").click()
    driver.find_element_by_link_text("Groups").click()
    driver.find_element_by_link_text(pageName).click()
#infinite see more posts loop
def more_posts_loop():
    
    elem = driver.find_elements_by_link_text("See More Posts")
    while len(elem) > 0:
        driver.find_element_by_link_text("See More Posts").click()
        elem = driver.find_elements_by_link_text("See More Posts")



fb_login()
page_nav("University of Michigan Class of 2022")
more_posts_loop()
