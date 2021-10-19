from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver')
#####Telegu songs List####
driver.get(r'https://wynk.in/music/packagesearch?q=telugu%20song&filter=SONG')
# p = driver.find_elements_by_id("websiteShimmering")
p = driver.find_elements_by_class_name("playlistWrapper")

# p = driver.find_elements_by_xpath("//a[contains(@href,'wynk.in/music/song/ramuloo-ramulaa/am_INA091916664')]")
# p.sort()
for i in p:
   print(i.text.strip('Ramuloo Ramulaa'))

