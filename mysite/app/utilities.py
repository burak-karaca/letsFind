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

   mcu = [i for i in driver.find_elements_by_css_selector('.vjtvke')]
   mcuText = [i.text for i in driver.find_elements_by_css_selector('.vjtvke')]
   try:
      for i in range(len(mcuText)):
         if 'Mikrokontrolery' in mcuText[i]:
            mcu[i].click()
         else:
            pass
   except:
      pass

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



   def getElements():
      elements = [c.text for c in driver.find_elements_by_css_selector(".A2sOrd")]
      elementOutput = len(elements)
      if elementOutput == 0:
         elements = [cc.text for cc in driver.find_elements_by_css_selector(".xsRiS")]
      return elements

   def getPrices():
      prices = [b.text for b in driver.find_elements_by_css_selector(".h1Wfwb")]
      pricesOutput = len(prices)
      if pricesOutput == 0:
         prices = [b.text for b in driver.find_elements_by_css_selector(".QIrs8")]
      return prices

   def getShop():
      shop = [a.text for a in driver.find_elements_by_css_selector(".a3H7pd")]
      shopOutput = len(shop)
      if shopOutput == 0:
         shop = [aa.text for aa in driver.find_elements_by_css_selector(".hy2WroIfzrX__merchant-name")]
      return shop

   def getLinks():
      links = [my_elem.get_attribute("href") for my_elem in driver.find_elements_by_css_selector("a.shntl")]
      linksOutput = len(links)
      if linksOutput == 0:
         links = [my_elemm.get_attribute("href") for my_elemm in driver.find_elements_by_css_selector("a.shntl")]
      return links

   def getImages():
      images = [img_src.get_attribute("src") for img_src in driver.find_elements_by_xpath("//div[@class='MUQY0']/img")]
      imagesOutput = len(images)
      if imagesOutput == 0:
         images = [img_srcc.get_attribute("src") for img_srcc in driver.find_elements_by_css_selector((".TL92Hc"))]
      return images

   p1 = getElements()
   p2 = getPrices()
   p3 = getShop()
   p4 = getLinks()
   p5 = getImages()

   l1 = [x for x in p1]
   l2 = [x for x in p2]
   l3 = [x for x in p3]
   l4 = [x for x in p4]
   l5 = [x for x in p5]


   page= driver.find_elements_by_css_selector(".fl")
   for abc in range(len(page)):
      try:
         page = driver.find_elements_by_css_selector(".fl")
         pageOutput = len(page)
         page[abc].click()
         if pageOutput > 1:
            pageEl = getElements()
            pagePr = getPrices()
            pageSh = getShop()
            pageLi = getLinks()
            pageIm = getImages()
            for x in pageEl:
               l1.append(x)
            for x in pagePr:
               l2.append(x)
            for x in pageSh:
               l3.append(x)
            for x in pageLi:
               l4.append(x)
            for x in pageIm:
               l5.append(x)
      except:
         pass

   elementsUpper = []
   filterSearch = data.upper().split()
   for i in l1:
      elementsUpper.append(i.upper())
   finalIndexing = [elementsUpper.index(str) for str in elementsUpper if any(sub in str for sub in filterSearch)]
   newElements = []
   newPrices = []
   newShop = []
   newLinks = []
   newImages = []

   for i in finalIndexing:
      newElements.append(l1[i])
      newPrices.append(l2[i])
      newShop.append(l3[i])
      newLinks.append(l4[i])
      newImages.append(l5[i])


   output = set()
   for x in newShop:
      output.add(x)
   sortfilteredLinks = sorted(output)
   x = list(zip(newElements, newPrices, newShop, newLinks, newImages))
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
