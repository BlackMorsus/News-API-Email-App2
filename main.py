import requests

api_key = "2a399d1986aa4ea6844cd521d8bdd9e7"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-06-23"
       "&sortBy=publishedAt&apiKey=2a399d1986aa4ea6844cd521d8bdd9e7")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and descriptions
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
