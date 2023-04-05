import requests
from bs4 import BeautifulSoup

def get_cos(ancestor, selector, atribute = None, return_list = False): 
    try:
        if return_list:
            return [tag.text.strip() for tag in ancestor.select(selector)].copy()
        if not selector:
            return ancestor(atribute)
        if atribute:
            return ancestor.select_one(selector)[atribute].strip()
        return ancestor.select_one(selector).text.strip()
    except AttributeError:
        return None
 
        
# product_code = input("Podaj kod produktu:")
product_code = "96685108"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
responce = requests.get(url)
page = BeautifulSoup(responce.text, "html.parser")
opinions = page.select("div.js_product-review")
all_opinions = []
for opinion in opinions:
    print(opinion["data-entry-id"])
    single_opinion = {
        "opinion_id": opinion["data-entry-id"],
        "author": opinion.select_one('span.user-post_author-name').text.strip(),
        "recommendation": opinion.select_one('spam.user-post_author-recomendation > recommended').text.strip(),
        "score": opinion.select_one('spam.user-post_score-count').text.strip(),
        "purchased": opinion.select_one('div.review-pz').text.strip(),
        "published_at": opinion.select_one('span.user-post__published > time:nth-child(1)')['datetime'].strip(),
        "purchased_at": opinion.select_one('span.user-post__published > time:nth-child(2)')['datetime'].strip(),
        "thumbs_up": opinion.select_one('button.vote-yes > span').text.strip(),
        "thumbs_down": opinion.select_one('button.vote-no > span').text.strip(),
        "content": opinion.select_one('div.user-post__text').text.strip(),
        "cons": [cons.text.strip() for cons in opinion.select('div.review-feature__col:has(>div.review-feature__title-negatives) > div.review-feature__item')],
        "pros": [pros.text.strip() for pros in opinion.select('div.review-feature__col:has(>div.review-feature__title-positives) > div.review-feature__item')],
    }
    all_opinions.append(single_opinion)

print(all_opinions)
print(type(opinion))
