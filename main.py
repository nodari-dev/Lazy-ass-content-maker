import requests
from bs4 import BeautifulSoup

# Make a request
page = requests.get(
    "https://magecloud.agency/website-design-manchester/")
soup = BeautifulSoup(page.content, 'html.parser')
landing = []

PageContent = soup.select('container_full')
for content in PageContent:
    text = content.select('p.landing-text')[0].text
    info = {
        "Text": text.strip()
        }
    landing.append(info)

print(landing)

# Steps for getting content:

# GET ALL HEADINGS WITH HTML TEXT INSIDE (<strong>)


# FIRST [".header-content"]
#   From [".header-text"] get h1 and p.landing-text
#
# SECOND [".container_full"]. Block with <h2> under header
#   From [".container"] get h2.landing (on some pages we don't have it)
# 
# THIRD  [".container_full"]. Block with <p> under header
#   From [".container"] get p.landing-text (on some pages we don't have it)
# 
# FOURTH [".main-container-landing"]. All main content is in these blocks
#   From [".text-container"] get h2.landing and p.landing-text
#
# FIFTH [".container_full"]. Block with <h2> above footer
#   From [".container"] get h2.landing (on some pages we don't have it)

# SIXTH [".container_full"]. Block with <h2> above footer
#   From [".container"] get p.landing-text (on some pages we don't have it