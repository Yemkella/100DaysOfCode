from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
upvotes = soup.find_all(name="span", class_="score")
article_texts = []
article_links = []
article_upvotes = []
for tag in articles:
    article_text = tag.getText()
    article_texts.append(article_text)
    article_link = tag.find("a")
    href = article_link.get("href")
    article_links.append(href)
for _ in upvotes:
    text = _.getText()
    split_text = text.split()
    article_upvotes.append(int(split_text[0]))

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])
print(article_upvotes[largest_index])


# # import lxml

# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')

# # all contents legible
# # print(soup.prettify())

# contents
# print(soup.title)

# # contents of title
# print(soup.title.string)

# # name of tag
# print(soup.title.name)

# # prints first anchor tag
# print(soup.a)

# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.getText())

# company_url = soup.select_one(selector="p a")
# print(company_url)

# name = soup.select_one("#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)