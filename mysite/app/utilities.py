from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time



def fetch_data(data,minPrice,maxPrice):
   PATH = "C:\Program Files (x86)\chromedriver.exe"
   options = Options()
   options.add_argument('--headless')
   options.add_argument('--disable-gpu')
   driver = webdriver.Chrome(PATH, chrome_options=options)
   driver.get("https://www.google.com/shopping")
   search = driver.find_element_by_name("q")
   search.send_keys(data)
   search.send_keys(Keys.RETURN)

   # featuresItemListPrices = [my_elem.text for my_elem in driver.find_elements_by_css_selector(".n3Kkaf")]
   # print(featuresItemListPrices)
   # featuresItemListPricesLinks = [my_elemmm.get_attribute("href") for my_elemmm in driver.find_elements_by_css_selector(".vjtvke")]
   # print(featuresItemListPricesLinks)

   try:
      minim = driver.find_element_by_name("lower")
      minim.send_keys(minPrice)
      maxim = driver.find_element_by_name("upper")
      maxim.send_keys(maxPrice)
      time.sleep(1)
      go = driver.find_element_by_class_name("sh-dr__prs")
      go.click()
   except:
      pass
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

   def getelements():

      elements = [c.text for c in driver.find_elements_by_css_selector(".A2sOrd")]
      prices = [b.text for b in driver.find_elements_by_css_selector(".Nr22bf")]
      shop = [a.text for a in driver.find_elements_by_css_selector(".a3H7pd")]
      links = [my_elem.get_attribute("href") for my_elem in driver.find_elements_by_css_selector("a.shntl")]
      images = [img_src.get_attribute("src") for img_src in driver.find_elements_by_xpath("//div[@class='MUQY0']/img")]

      imagesOutput = len(images)
      elementOutput = len(elements)
      shopOutput = len(shop)
      linksOutput = len(links)

      if elementOutput == 0:
         elements = [cc.text for cc in driver.find_elements_by_css_selector(".xsRiS")]
      if shopOutput == 0:
         shop = [aa.text for aa in driver.find_elements_by_css_selector(".hy2WroIfzrX__merchant-name")]
      if linksOutput == 0:
         links = [my_elemm.get_attribute("href") for my_elemm in driver.find_elements_by_css_selector("a.shntl")]
      if imagesOutput == 0:
         images = [img_srcc.get_attribute("src") for img_srcc in driver.find_elements_by_css_selector((".TL92Hc"))]
      return elements,prices,shop,links,images

   p1 = getelements()

   l1 = [x for x in p1[0]]
   l2 = [x for x in p1[1]]
   l3 = [x for x in p1[2]]
   l4 = [x for x in p1[3]]
   l5 = [x for x in p1[4]]

   page= driver.find_elements_by_css_selector(".fl")
   pageOutput = len(page)

   # for abc in range(pageOutput):
   #    try:
   #       page = driver.find_elements_by_css_selector(".fl")
   #       pageOutput = len(page)
   #       page[abc].click()
   #       if len(p1) > 1:
   #          for x in p1[0]:
   #             l1.append(x)
   #          for x in p1[1]:
   #             l2.append(x)
   #          for x in p1[2]:
   #             l3.append(x)
   #          for x in p1[3]:
   #             l4.append(x)
   #          for x in p1[4]:
   #             l5.append(x)
   #    except:
   #       pass

   output = set()
   for x in l3:
      output.add(x)
   sortfilteredLinks = sorted(output)
   x = list(zip(l1, l2, l3, l4, l5))
   ls = []
   for i in x:
      dc = {}
      dc['elements'] = i[0]
      dc['prices'] = i[1]
      dc['shop'] = i[2]
      dc['links'] = i[3]
      dc['images'] = i[4]
      ls.append(dc)

   x1 = list(zip(sortfilteredLinks))
   eshops = []
   for y in x1:
      dc2 = {}
      dc2['sortfilteredLinks'] = y[0]
      eshops.append(dc2)
   sumofTheProducts = []
   sumofTheProducts.append(ls)
   sumofTheProducts.append(eshops)
   return sumofTheProducts
