#Library imports
import requests
from send_email import send_email

# News API endpoint and parameters
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-12-17&sortBy=publishedAt&apiKey=0a987893d8274d26ad74afaf08ffd35b"
api_key = "0a987893d8274d26ad74afaf08ffd35b"

# Make a request to the News API
request = requests.get(url)

# Get the JSON content from the response
content = request.json()

body = ""

# Print the titles and descriptions of the articles
for article in content["articles"]:
    if article['title'] != None and article['description'] != None:
        body = body + article['title'] + ": " + "\n" + article['description'] + 2*"\n"
 
body = body.encode('utf-8') 
send_email(body)