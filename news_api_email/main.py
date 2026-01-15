import requests

url = "https://newsapi.org/v2/everything?q=tesla&from=2025-12-15&sortBy=publishedAt&apiKey=0a987893d8274d26ad74afaf08ffd35b"
api_key = "0a987893d8274d26ad74afaf08ffd35b"

request = requests.get(url)
content = request.json()
##print(content)

for article in content["articles"]:
    print(article['title'])
    print(article['description'])