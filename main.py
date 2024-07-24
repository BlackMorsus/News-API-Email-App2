import requests
from send_email import send_email

api_key = "2a399d1986aa4ea6844cd521d8bdd9e7"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-06-23"
       "&sortBy=publishedAt&apiKey=2a399d1986aa4ea6844cd521d8bdd9e7")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and descriptions
body = ""
for article in content["articles"]:
    if article["title"] is not None
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)