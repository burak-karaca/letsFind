from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def fetch_data(data,minPrice,maxPrice):
   PATH = "C:\Program Files (x86)\chromedriver.exe"
   driver = webdriver.Chrome(PATH)

   driver.get("https://www.google.com/shopping")
   search = driver.find_element_by_name("q")
   search.send_keys(data)
   search.send_keys(Keys.RETURN)
   # try:
   #    minim = driver.find_element_by_name("lower")
   #    minim.send_keys(minPrice)
   #    maxim = driver.find_element_by_name("upper")
   #    maxim.send_keys(maxPrice)
   #    time.sleep(1)
   #    go = driver.find_element_by_class_name("sh-dr__prs")
   #    go.click()
   # except:
   #    pass
   # try:
   #    clickPrices = driver.find_element_by_css_selector(".vkYnff")
   #    clickPrices.click()
   #    sortingPrices = driver.find_elements_by_css_selector(".kH0Dhc")
   #    sortPriceArray = []
   #    for d in sortingPrices:
   #       sortPriceArray.append(d)
   #    time.sleep(1)
   #    lengthIf = len(sortPriceArray)
   #    if lengthIf == 3:
   #       sortPriceArray[1].click()
   #    elif lengthIf == 4:
   #       sortPriceArray[2].click()
   # except:
   #    pass

   time.sleep(1)
   elements = [c.text for c in driver.find_elements_by_css_selector(".A2sOrd")]
   prices = [b.text for b in driver.find_elements_by_css_selector(".Nr22bf")]
   shop = [a.text for a in driver.find_elements_by_css_selector(".a3H7pd")]
   links = [my_elem.get_attribute("href") for my_elem in driver.find_elements_by_css_selector(".shntl")]
   images = [img_src.get_attribute("src") for img_src in driver.find_elements_by_xpath("//div[@class='MUQY0']/img")]

   imagesOutput = len(images)
   elementOutput = len(elements)
   shopOutput = len(shop)
   linksOutput = len(links)

   if elementOutput == 0:
      elements = [cc.text for cc in driver.find_elements_by_css_selector(".xsRiS")]
      print(elements)
   else:
      print("nothing to show")
   if shopOutput == 0:
      shop = [aa.text for aa in driver.find_elements_by_css_selector(".shntl")]
      print(shop)
   else:
      print("nothing to show")
   if linksOutput == 0:
      links = [my_elemm.get_attribute("href") for my_elemm in driver.find_elements_by_css_selector("a.shntl")]
      print(links[0])
   else:
      print("nothing to show")
   if imagesOutput == 0:
      images = [img_srcc.get_attribute("src") for img_srcc in driver.find_elements_by_css_selector((".TL92Hc"))]
      print(images)
   else:
      print("nothing to show")


   x = list(zip(elements, prices, shop, links, images))
   ls = []
   for i in x:
      dc = {}
      dc['element'] = i[0]
      dc['prices'] = i[1]
      dc['shop'] = i[2]
      dc['link'] = i[3]
      dc['images'] = i[4]
      ls.append(dc)
   return ls


