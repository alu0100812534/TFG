from selenium import webdriver
from time import sleep

i = 5
a = 0
browser = webdriver.Firefox()
browser.get('https://www.youtube.com/watch?v=qbYxB0O1o4E')
while 5 < 6:

    #browser.save_screenshot('imgs/screenie0' + str(a) + '.png')
    browser.get_screenshot_as_png()
    a += 1

browser.quit()
