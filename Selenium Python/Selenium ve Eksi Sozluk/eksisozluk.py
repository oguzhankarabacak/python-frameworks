from selenium import webdriver
import time
import random


browser=webdriver.Firefox()
url="https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="

entries=[]
pageCount=1
entryCount=1

while pageCount <= 10:
    randomCount=random.randint(1,1623)
    newUrl=(url+str(randomCount))
    browser.get(newUrl)
    elements = browser.find_elements_by_css_selector('.content')
    for element in elements:
        entries.append(element.text)
    time.sleep(3)
    pageCount += 1

with open("entries.txt","w",encoding="UTF-8") as file:
    for entry in entries:

        file.write(str(entryCount)+".\n"+entry+"\n")
        entryCount += 1

browser.close()



