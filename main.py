"""
This set of python codes are used to extract news information using API
"""

import requests as rq
from send_email import send_email

api_key = "80fc704b938b4540811be9dc10c79508"

url = "https://newsapi.org/v2/everything?q=tesla&from=2024-04-25&sortBy=publishedAt&api" \
      "Key=80fc704b938b4540811be9dc10c79508"

#Make a request
request = rq.get(url)

# Got a dictionary
content = request.json()

#Access the article titles and description
email_body = ""
for article in content["articles"]:
    if article["title"] is not None:
        email_body = email_body + article["title"] + "\n" + article["description"] + 2*"\n"

email_body = email_body.encode("utf-8")

send_email(message=email_body)