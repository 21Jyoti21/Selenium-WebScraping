from bs4 import BeautifulSoup
import os
import pandas as pd

d={'title':[],'price':[],'link':[]}
for file in os.listdir("data"):
    try:
        with open(f"data/{file}", encoding="utf-8") as f:
            html_doc = f.read()

        soup = BeautifulSoup(html_doc, 'html.parser')

        title_tag = soup.find("span", {"class": "a-size-medium"})
        title = title_tag.get_text(strip=True) if title_tag else "N/A"

        link_tag = soup.find("a", {"class": "a-link-normal"})
        link = "https://www.amazon.in" + link_tag["href"] if link_tag and link_tag.has_attr("href") else "N/A"

        p=soup.find("span",attrs={"class":'a-price-whole'})
        price=p.get_text()

        d['title'].append(title)
        d['price'].append(price)
        d['link'].append(link)
       
    except Exception as e:
        print(e)
df=pd.DataFrame(data=d)
df.to_csv("data.csv")
