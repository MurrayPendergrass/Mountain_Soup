import requests
from bs4 import BeautifulSoup

def overwrite():
    url = "https://www.mountainproject.com/area/110928184/stuart-enchantments"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    data = []

    for a in soup.select("div.lef-nav-row a"):
        url2 = a.get('href')
        page2 = requests.get(url2)
        soup2 = BeautifulSoup(page2.text, "html.parser")

        table = soup2.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="left-nav-route-table")

        if type(table) == type(None):
            table2 = soup2.select("div.lef-nav-row a")
            data.append(a.get_text(strip=True) + ":" + str(len(table2)))

        else:
            table2 = soup2.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="left-nav-route-table") 
            data.append(a.get_text(strip=True) + ":" + str(len(table2)))

    f = open('counts.txt','w')
    f.write('\n'.join(data))
    f.close()

   

  

  
    




