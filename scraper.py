import requests
from bs4  import BeautifulSoup


# product_code = input("Podaj kod produktu:")
product_code = "96685108"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
responce = requests.get(url)
page = BeautifulSoup(responce.text, "html.parser")
options = page.select("div.js_product-review")

for option in options:
    print(option ["data-entry-id"])

