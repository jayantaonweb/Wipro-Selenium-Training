from bs4 import BeautifulSoup
import requests

html = '''
<html>
    <head>
    <title>My Page</title>
    </head>
    <body>

        <h1>Welcome</h1>
        <h2>Sub Heading</h2>

        <p>This is paragraph 1.</p>
        <p>This is paragraph 2.</p>

        <a href="https://google.com">Google</a>
        <a href="https://openai.com">OpenAI</a>

        <b>Bold Text</b>

        <img src="image1.jpg">
        <img src="image2.png">

        <table border="1">
            <tr><th>Name</th><th>Age</th></tr>
            <tr><td>Rahul</td><td>21</td></tr>
            <tr><td>Amit</td><td>22</td></tr>
        </table>

    </body>
</html>
'''

soup = BeautifulSoup(html, "html.parser")

#Q1. Parse HTML – Extract title and h1
print("Title:", soup.title.text)
print("H1:", soup.h1.text)

#Q2. Extract All Paragraphs
paragraphs = soup.find_all("p")
for para in paragraphs:
    print(para.text)

#Q3. Extract All Links and Count

links = soup.find_all("a")

print("total count of links:", len(links))

for link in links:
    print(link.text, " " , link["href"])

#Q4.Extract all attributes
# extract all href
for a in soup.find_all("a"):
    print(a.get("href"))
#extract all the images
for img in soup.find_all("img"):
    print(img.get("src"))

#Q5.extract first h2
h2 = soup.find("h2")
if h2:
    print("First H2 tag:", h2.text)

#Q6. extract bold text

bold = soup.find_all("b")
for b in bold:
    print("Bolf texts:", b.text)

#Q7. extract all href

hrefs = [a["href"] for a in soup.find_all("a")]
print("all hrefs:", hrefs)

#Q8. get all text without tags

text = soup.get_text()
print("Texts without tags:", text.strip())

#Q9. extract title from real website

url = "https://www.google.com"
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")
print("real website title:", soup.title.text)

#Q10. extract all headings

for i in range(1, 7):
    headings = soup.find_all(f"h{i}")

    for h in headings:
        print(f"h{i}:", h.text)

#Q11. extract table data
table = soup.find("table")
rows = table.find_all("tr")

for row in rows:
    cols = row.find_all(["td", "th"])
    data = [col.text for col in cols]
    print("Table Data:", data)
#Q12. extract image

images = soup.find_all("img")
for img in images:
    print("Image:", img.get("src"))