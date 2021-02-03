import requests
from bs4 import BeautifulSoup as bs

page = requests.get(
    "https://magecloud.agency/website-design-manchester/")
soup = bs(page.content, 'html.parser')

#CONTENT ARRAYS
HeaderHeading = []
HeaderParagraph = []

UnderHeaderHeading = []
UnderHeaderParagraph = []

MainContainerLanding = []

FooterHeading = []
FooterParagraph = []


products = soup.select('div.main-container-landing')
for elem in products:
    title = elem.select('p')[0].text
    info = {
        "title": title.strip()
    }
    MainContainerLanding.append(info)

print(MainContainerLanding)

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