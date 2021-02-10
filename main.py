import requests
from bs4 import BeautifulSoup as bs
import random
import presets

# INPUT ARRAYS
websitesCityList = [] # Min name of cities for dict
websitesCityNames = [] # Full names of cities
websitesDict = {}

city = 'Test'

headContent = {
    'Title':
    {
        'TitleDesign': '🥇 Web Design Agency in ' + city + '. Web designers in ' + city,
        'TitleDev': '🥇 Web Development Agency in ' + city + '. Web developers in ' + city,
        'TitleMagento': '🥇 Magento Web Development & eCommerce consulting agency in ' + city,
        'TitleShopify': '🥇 Shopify Development Agency in ' + city + '. Web developers in ' + city,
        'TitleWP': '🥇 WordPress & WooCommerce Development Agency in ' + city + '. Web developers in ' + city
    },
    'Meta':
    {
        'MetaDesign': 'Web design agency in ' + city + ' ✅ with full-stack front-end back-end developers in ' + city + '⚡',
        'MetaDev': 'Web development agency in ' + city + ' ✅ with full-stack frontend backend developers in ' + city + '⚡',
        'MetaMagento': 'Magento agency in ' + city + ' ✅ with certified developers and solution specialists ready to start today. ⚡We design, develop and support.',
        'MetaShopify': 'Shopify agency in ' + city + ' ✅ with full-stack frontend backend developers in ' + city + '.⚡',
        'MetaWP': 'WordPress & WooCommerce agency in ' + city + ' ✅ with full-stack frontend backend developers in ' + city + '. ⚡'
    }
}

# WRITE ALL STAGES OF GETTING AND COLLECTING

def contentGenerator():

    # TODO: in main function run this function with arguments 'Categories' and smth else...
    # TODO: Solve problem with categories and text replacement (design, dev) => KEYWORDS
    """
    This function gets links from txt file
    Get names of cities from links
    Generate dict of links and cities
    """
    try:
        websitesFile = open("websites.txt", "r")
    except NameError:
        print('No file named "websites.txt"')
    else:
        for line in websitesFile:
            websiteLink = line.strip()

            # Parse all HTML page
            page = requests.get(websiteLink)
            websiteContent = bs(page.content, 'html.parser')

            # Write all changes to dictionary

            websitesDict[websiteLink] = {
                "City": getCityName(websiteLink),
                "Category": getCategory(websiteLink),
                # "underHeaderParagraph": 'Paragraph',
                # "mainContainerLanding": "Content",

                # "Content": websiteContent
            }

            # We use these functions to get all content from pages
            # Sort and add them to websiteDict

            getUnderHeader(websiteLink, websiteContent)
            getMainContainer(websiteLink, websiteContent)

        # print(websitesDict.items())
        for key, value in websitesDict.items():
            print(str(key) + ' : ' + str(value) + '\n')
    finally:
        websitesFile.close()


def getCityName(websiteProc):
    """
    This function get city name from link
    First we need to remove chars for presets.checks
    Then clean text and set correct capitalize
    """
    websitesCity = str(websiteProc)

    # Remove checking elements
    for check, empty in presets.checks.items():
        if check in websitesCity:
            websitesCity = websitesCity.replace(check, empty)
            break

    # Clean text
    for key, value in presets.charToReplace.items():
        websitesCity = websitesCity.replace(key, value)

        # Capitalize first and last word
        websiteCityCapitalize = websitesCity.split()

        # Capitalize first word
        websiteCityCapitalize[0] = websiteCityCapitalize[0].capitalize()

        # Capitalize last word if length > 1
        if len(websiteCityCapitalize) > 1:
            websiteCityCapitalize[-1] = websiteCityCapitalize[-1].capitalize()
            break
        websiteCity = ' '.join(websiteCityCapitalize)

    return websiteCity


def getCategory(websiteProc):
    """
    This function identifying category from each link
    """
    for key, category in presets.categoryDict.items():
        if key in websiteProc:
            return category
            break


def getMainContainer(linkProc, websiteProcContent):
    """
    This function gets all headings and paragraphs
    from <div class="main-container-landing">
    And write them into websitesDict
    """
    elements = websiteProcContent.find_all('div', class_='main-container-landing')

    # 'n' variable is a count of found elements with same type
    for n, element in enumerate(elements, start=0):
        # here we find heading
        heading = element.find('h2').text

        # here we find paragraph
        paragraph = element.find('p').text
        # print(heading + '\n' + paragraph + '\n')

        # we write every heading and paragraph into websiteDict with special number
        # to see if they are in one block
        websitesDict[linkProc]['mainHeading' + str(n)] = heading
        websitesDict[linkProc]['mainParagraph' + str(n)] = paragraph


def getUnderHeader(linkProc, websiteProcContent):
    """
    This function get heading and paragraph from div='underheader'
    Then write changes into websiteDict
    """
    elements = websiteProcContent.find_all('div', class_='container_full underheader')
    if len(elements) != 0:
        for textEl in elements:
            if 'h2' in str(textEl):
                # First we get <h2> text and if exist such element
                heading = textEl.text
                # 'n' variable is a count of found elements with same type
                for n, element in enumerate(elements, start=0):
                    websitesDict[linkProc]['underHeaderHeading' + str(n)] = heading
                    break
            else:
                # First we get <p> text and if exist such element
                paragraph = textEl.text
                for n, element in enumerate(elements, start=0):
                    websitesDict[linkProc]['underHeaderParagraph' + str(n)] = paragraph
                    break
    else:
        print('No block named underheader')


def filterTitle(categoryTitle, categoryMeta):
    """
    This function select title and meta
    for generating final dict of info
    """
    print(headContent['Title'][categoryTitle])
    print(headContent['Meta'][categoryMeta])

if __name__ == '__main__':
    contentGenerator()
    # filterTitle('TitleDev', 'MetaDev')

    # CityList = [str(item) for item in input("Enter list of cities : ").split()]
    # for city in CityList:
    #     for category in CategoryList:


