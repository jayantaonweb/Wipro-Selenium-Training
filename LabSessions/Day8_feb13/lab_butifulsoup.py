

"""
Install and import BeautifulSoup from the bs4 module.
Write a simple program to parse a small HTML string.
Given this HTML:
Extract the title text.
Extract the <h1> text.
Extract the paragraph text.
Write a program to:
Find the first <a> tag.
Print its href attribute.
Use .prettify() to format parsed HTML.
What is the difference between:
find()
find_all()
"""
import requests
from bs4 import BeautifulSoup
html_doc="""<html>
  <head><title>Test Page</title></head>
  <body>
    <h1>Welcome</h1>
    <p>This is a paragraph.</p>
    <a href="https://example.com">Click here</a>
  </body>
  </html>
"""

soup =BeautifulSoup(html_doc,"html.parser")

print("Title:", soup.title.string)

print("H1:", soup.h1.string)

print("Paragraph:", soup.p.string)

first_link = soup.find("a")
print("href:", first_link["href"])

print(soup.prettify())

print(soup.find("p")) #stops at the first match.
print(soup.find_all("p")) #searches entire document and returns all matches.




'''
.Scrape product details from an e-commerce sample page:
Product name
Price
Rating
Availability
Extract all image URLs from a webpage.
 '''

url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
headers = {
    # user - agent - who is making the request and from where
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)

# parse the html
soup = BeautifulSoup(response.text, features="html.parser")

p_name = soup.find("h1").text

print("Product Name:", p_name)

price = soup.find("p",class_="price_color").text
print("Price:", price)

rating_tag = soup.find("p", class_="star-rating")
rating = rating_tag["class"][1]
print("Rating:", rating)

availability = soup.find("p", class_="instock availability").text.strip()
print("Availability:", availability)

images = soup.find_all("img")

image_urls = []

for img in images:
    img_url = img.get("src")

    # Convert relative URLs to full URLs
    full_url = "http://books.toscrape.com/" + img_url.replace("../", "")
    image_urls.append(full_url)

print("Image URLs:")
for url in image_urls:
    print(url)