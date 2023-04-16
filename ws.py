from bs4 import BeautifulSoup
import re
import requests
from urllib.parse import urljoin

brand  = input("Give me the name of the brand: ")

url_1 = f"https://www.flipkart.com/search?q=running+shoes&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&p%5B%5D=facets.brand%255B%255D%3D{brand}"
result_1 = requests.get(url_1).text
doc_1 = BeautifulSoup(result_1, "html.parser")

page_text_1 = doc_1.find_all(class_="ge-49M")
pages_1 = int(str(page_text_1[-1]).split(">")[-2].split("<")[0])

items_found_1={}
for page in range(1,pages_1+1):
    url_1 = f"https://www.flipkart.com/search?q=running+shoes&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&p%5B%5D=facets.brand%255B%255D%3D{brand}&page={page}"
    result_1 = requests.get(url_1).text
    doc_1 = BeautifulSoup(result_1, "html.parser")

    items_1 = doc_1.find_all(string=re.compile("Running"))
    for item in items_1:
        try:
            link_tag_1 = item.find_parent("a")
            parent_1 = link_tag_1.find_parent(class_="_1xHGtK _373qXS")
            price_1 = parent_1.find(class_="_30jeq3").string
            symbol_1 = price_1[0]
            if link_tag_1 is not None:
                link_1 = link_tag_1.get("href")
                if link_1 is not None:
                    absolute_url_1 = urljoin(url_1, link_1)
                    
            items_found_1[item] = {"price": int(price_1.replace(",","").replace(price_1[0],"")), "link":absolute_url_1}
        except:
            continue


url  = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=running+shoes&_sacat=0&Brand={brand}"
result = requests.get(url).text
doc = BeautifulSoup(result,"html.parser")


page_text = doc.find_all(class_="pagination__item")
pages = int(str(page_text[-1]).split("<")[-3].split(">")[1])


items_found_2={}

for page in range(1,pages+1):
    url  = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=running+shoes&_sacat=0&Brand={brand}&_pgn={page}"
    result = requests.get(url).text
    doc = BeautifulSoup(result,"html.parser")
    div = doc.find(class_="srp-river-main clearfix")

    try:
        items = div.find_all(string=re.compile("Running"))
    except:
        continue
    for item in items:
        
        try:
            link_tag = item.find_parent("a")
            parent = link_tag.find_parent(class_="s-item__wrapper clearfix")
            price = parent.find(class_="s-item__price").string
            symbol = price[0]
            if link_tag is not None:
                link = link_tag.get("href")
                if link is not None:
                    absolute_url = urljoin(url, link)
                    
            
            items_found_2[item]={"price":float(price.replace("$",""))*82,"link":absolute_url}
        except:
            continue


items_found_1.update(items_found_2)
sorted_items = sorted(items_found_1.items(),key = lambda x:x[1]['price'])


f = open('result.txt','w')
for item in sorted_items:
    f.write(item[0] + "\n")
    f.write(f"{symbol_1}{item[1]['price']}\n")
    f.write(item[1]['link'] + "\n")
    f.write("-----------\n")

f.close()





              


    



      
      

        







