from selenium import webdriver
import time


browser=webdriver.Firefox()
browser.get("https://twitter.com/")
time.sleep(1)

giris_yap=browser.find_element_by_xpath("//*[@id='doc']/div/div[1]/div[1]/div[2]/div[2]/div/a[2]")

giris_yap.click()

time.sleep(1)

username=browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input")
password=browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input")
account_giris_yap=browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button")

username.send_keys("@oguz42kara")
password.send_keys("cccgfreis1998")
time.sleep(1)
account_giris_yap.click()
time.sleep(1)
searchArea=browser.find_element_by_xpath("//*[@id='search-query']")
searchButton=browser.find_element_by_xpath("//*[@id='global-nav-search']/span/button")
searchArea.send_keys("#yazılımayolver")
time.sleep(1)
searchButton.click()
time.sleep(1)


lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(5)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True

likeButtons=browser.find_elements_by_css_selector(".ProfileTweet-actionButtonUndo.ProfileTweet-action--unfavorite.u-linkClean.js-actionButton.js-actionFavorite")

for i in likeButtons:
    try:
        time.sleep(1)
        i.click()

    except Exception:
        print("bir hata oluştu")