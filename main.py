"""
This set of python codes are used to extract news information using API
"""

import requests as rq
from send_email import send_email

# Create a variable called topic to decide what particlaur topics to extract and avoid tampering with the url.
# The topic is set to tesla for this test run.
topic = "tesla"

api_key = "80fc704b938b4540811be9dc10c79508"

# Added "&language=en" at the end of the url to extract only news in english language
# Adjusted the 2nd line with f block to make the extracted topic dynamic
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \   
      "from=2024-04-27" \
      "&sortBy=publishedAt&" \
      "apiKey=80fc704b938b4540811be9dc10c79508&" \
      "language=en"

#Make a request
request = rq.get(url)

# Got a dictionary
content = request.json()

# Access the article titles, description, and links to read further
email_body = ""

# Iterate to pick only the first 20 emails
for article in content["articles"][:20]:

    # Skip the article if the title is None
    if article["title"] is None:
        continue

    subject = "Subject: Today's News"
    title = article["title"]
    description = article["description"] if article["description"] else ""
    email_body += f"{subject}\n{title}\n{description}\n{article['url']}\n\n"

# Convert the email body to encode the message into email format
email_body = email_body.encode("utf-8")

send_email(message=email_body)


