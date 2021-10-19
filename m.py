from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver')
#####Telegu songs List####
driver.get(r'https://wynk.in/music/packagesearch?q=telugu%20song&filter=SONG')

p = driver.find_elements_by_class_name("playlistWrapper")
arr = []
arr1= []
for i in p:
    o = i.text.strip()
    arr.append(o)
    mystring = "".join(arr)
    str1 = mystring.replace('\n',',')
    li = list(str1.split(','))
    m = []
    for ch in li:
        if ch[0] == "R":
            m.append(ch)
    print(m)