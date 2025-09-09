# from bs4 import BeautifulSoup
# import os

# d={'title':[1,2],'price':[3,4],'link':[1,2]}

# for file in os.listdir("data"):
#     with open(f"data/{file}") as f:
#         html_doc=f.read()
#     soup = BeautifulSoup(html_doc, 'html.parser')
#     t=soup.find("h2")
#     if not t:
#         continue
#     title=t.get_text()
#     print(title)

#     l=t.find("a")
#     link="https://amazon.in/"+l['href'] if l and l.has_attr("href") else None
#     print(title,link)
#     break
#     # print(soup.prettify())


from bs4 import BeautifulSoup
import os
import pandas as pd

d={'title':[],'price':[],'link':[]}
for file in os.listdir("data"):
    try:
        with open(f"data/{file}", encoding="utf-8") as f:
            html_doc = f.read()

        soup = BeautifulSoup(html_doc, 'html.parser')

        # Title
        title_tag = soup.find("span", {"class": "a-size-medium"})
        title = title_tag.get_text(strip=True) if title_tag else "N/A"

        # Link
        link_tag = soup.find("a", {"class": "a-link-normal"})
        link = "https://www.amazon.in" + link_tag["href"] if link_tag and link_tag.has_attr("href") else "N/A"

        p=soup.find("span",attrs={"class":'a-price-whole'})
        price=p.get_text()

        d['title'].append(title)
        d['price'].append(price)
        d['link'].append(link)
        # print(title, link ,price)
        # break
    except Exception as e:
        print(e)
df=pd.DataFrame(data=d)
df.to_csv("data.csv")