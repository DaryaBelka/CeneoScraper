import json
import requests
from bs4 import BeautifulSoup

def get_element(ancestor, selector = None, attribute = None, return_list = False): 
    try:
        if return_list:
            return [tag.text.strip() for tag in ancestor.select(selector)].copy()
        if not selector and attribute:
            return ancestor[attribute]
        if attribute:
            return ancestor.select_one(selector)[attribute].strip()
        return ancestor.select_one(selector).text.strip()
    except AttributeError:
        return None
 
        

selectors = {
        "opinion_id": [None, ["data-entry-id"]],
        "author": ["span.user-post__author-name"].text.strip(),
        "recommendation": ["span.user-post_author-recomendation > recommended"].text.strip(),
        "score": ["span.user-post__score-count"].text.strip(),
        "purchased": ["div.review-pz"].text.strip(),
        "published_at": ["span.user-post__published > time:nth-child(1)", 'datetime'].strip(),
        "purchased_at": ["span.user-post__published > time:nth-child(2)", 'datetime'].strip(),
        "thumbs_up": ["button.vote-yes > span"].text.strip(),
        "thumbs_down": ["button.vote-no > span"].text.strip(),
        "content": ["div.user-post__text"].text.strip(),
        "pros": ["div.review-feature__col:has(>div.review-feature__title--positives) > div.review-feature__item", None, True],
        "cons": ["div.review-feature__col:has(>div.review-feature__title--negatives) > div.review-feature__item", None, True],
}
    

# product_code = input("Podaj kod produktu:")
product_code = "96685108"
page_no = 1
while():
    url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
    responce = requests.get(url)

    page = BeautifulSoup(responce.text, "html.parser")
    print("Test :",  get_element(page))
    opinions = page.select("div.js_product-review")
    all_opinions = []
    for opinion in opinions:
        single_opinion = {}
        for key, value in selector.items(opinion, value):
            single_opinion[key] = get_element()
        all_opinions.append(single_opinion)


with open(f".opinions/{product_code}.json", "w", enconding = "UTF-8") as jf:
    json.jump(all_options, jf, indent = 4, ensure_ascii=False)


