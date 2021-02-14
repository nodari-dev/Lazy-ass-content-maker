import requests
from bs4 import BeautifulSoup as bs
import random
import presets

# INPUT ARRAYS

# Min name of cities for dict
websitesCityList = []

# Full names of cities
websitesCityNames = []

websitesDict = {}
resultDict = {}

cityName = 'TEST CITY'

categoryList = ['wordpress', 'magento', 'shopify', 'development', 'design']
headContent = {
    'title':
        {
            'design': '🥇 Web Design Agency in ' + cityName + '. Web designers in ' + cityName,
            'development': '🥇 Web Development Agency in ' + cityName + '. Web developers in ' + cityName,
            'magento': '🥇 Magento Web Development & eCommerce consulting agency in ' + cityName,
            'shopify': '🥇 Shopify Development Agency in ' + cityName + '. Web developers in ' + cityName,
            'wordpress': '🥇 WordPress & WooCommerce Development Agency in ' + cityName + '. Web developers in ' + cityName
        },
    'meta':
        {
            'design': 'Web design agency in ' + cityName + ' ✅ with full-stack front-end back-end developers in ' + cityName + '⚡',
            'development': 'Web development agency in ' + cityName + ' ✅ with full-stack frontend backend developers in ' + cityName + '⚡',
            'magento': 'Magento agency in ' + cityName + ' ✅ with certified developers and solution specialists ready to start today. ⚡We design, develop and support.',
            'shopify': 'Shopify agency in ' + cityName + ' ✅ with full-stack frontend backend developers in ' + cityName + '.⚡',
            'wordpress': 'WordPress & WooCommerce agency in ' + cityName + ' ✅ with full-stack frontend backend developers in ' + cityName + '. ⚡'
        }
}

headerContent = {
    "heading":
        {
            'design': 'Web design agency in <strong>' + cityName + '</strong> with top-rated designers, developers, and marketing managers in <strong>' + cityName + '</strong>',
            'development': 'Web development agency in <strong>' + cityName + '</strong> with top-rated full-stack developers',
            'magento': 'Magento Agency in <strong>' + cityName + '</strong>. Expert Magento Web Development in <strong>' + cityName + '</strong>',
            'shopify': 'Shopify development agency in <strong>' + cityName + '</strong> with top-rated full-stack developers',
            'wordpress': 'Wordpress &amp; WooCommerce development agency in <strong>' + cityName + '</strong> with top-rated full-stack developers'
        },
    "paragraph":
        {
            'design': 'We provide full-stack developers in ' + cityName + '. Our agency support clients around Manchester and surrounding areas',
            'development': 'We provide full-stack development and support service in ' + cityName + ' with a primary focus on month-by-month improvements to store resulting in better performance, rankings and revenue.',
            'magento': 'We provide full-stack Magento development and support service in ' + cityName + ' with a primary focus on month-by-month improvements to store resulting in better performance, rankings and revenue.',
            'shopify': 'We provide full-stack Shopify development and support service ' + cityName + ' with a primary focus on month-by-month improvements to store resulting in better performance, rankings and revenue.',
            'wordpress': 'We provide full-stack Wordpress & WooCommerce developers in ' + cityName + '. Our WordPress & WooCommerce agency support clients around ' + cityName + ' and surrounding areas'
        }
}

mainContainer = {
    "design":
        {
            "headingOne": 'Give Your Competition a <strong>Run for Its Money</strong>',
            "headingTwo": 'The MageCloud Web <strong>Web Design Difference</strong>'
        },
    "development":
        {
            "headingOne": 'Back-end <strong>Development</strong>',
            "headingTwo": 'Front-end <strong>Development</strong>',
            "headingThree": "Platform <strong>Integrations</strong>",
            "headingFour": "Plugin <strong>Development</strong>"
        },
    "magento":
        {
            "headingOne": 'Your Magento Ecommerce <br> Development Partner in <strong>' + cityName + '</strong>',
            "headingTwo": 'Magento Ecommerce Design <br> in <strong>' + cityName + '</strong>',
            "headingThree": 'Creative Marketing Strategy for <br> Magento in <strong>' + cityName + '</strong>'
        },
    "shopify":
        {
            "headingOne": 'Back-end <strong>Development</strong>',
            "headingTwo": 'Front-end <strong>Development</strong>',
            "headingThree": "Platform <strong>Integrations</strong>",
            "headingFour": "Plugin <strong>Development</strong>"
        },
    "wordpress":
        {
            "headingOne": 'Back-end <strong>Development</strong>',
            "headingTwo": 'Front-end <strong>Development</strong>',
            "headingThree": "Platform <strong>Integrations</strong>",
            "headingFour": "Plugin <strong>Development</strong>"
        }
}

def contentGenerator():
    # TODO: in main function run this function with arguments 'Categories' and smth else...
    #  Solve problem with categories and text replacement (design, dev) => KEYWORDS
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
            }

            # We use these functions to get all content from pages
            # Sort and add them to websiteDict
            getUnderHeader(websiteLink, websiteContent)
            getMainContainer(websiteLink, websiteContent)
            getFooter(websiteLink, websiteContent)

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


def getUnderHeader(linkProc, websiteProcContent):
    """
    This function get heading and paragraph from div='underheader'
    Then write changes into websiteDict
    """
    elements = websiteProcContent.find_all('div', class_='container_full underheader')
    try:
        elements[0]
    except IndexError:
        print('No block named underheader')
    else:
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


def getMainContainer(linkProc, websiteProcContent):
    """
    This function gets all headings and paragraphs
    from <div class="main-container-landing">
    And write them into websitesDict
    """
    elements = websiteProcContent.find_all('div', class_='main-container-landing')
    try:
        elements[0]
    except NameError:
        print('No div with class "main-container-landing"')
    else:
        # 'n' variable is a count of found elements with same type
        for n, element in enumerate(elements, start=0):
            # here we find heading
            heading = element.find('h2').text

            # here we find paragraph
            paragraph = element.find('p').text

            # we write every heading and paragraph into websiteDict with special number
            # to see if they are in one block
            websitesDict[linkProc]['mainHeading' + str(n)] = heading
            websitesDict[linkProc]['mainParagraph' + str(n)] = paragraph


def getFooter(linkProc, websiteProcContent):
    """
    This function get heading and paragraph from div='abovefooter'
    Then write changes into websiteDict
    """
    elements = websiteProcContent.find_all('div', class_='container_full above-footer')
    try:
        elements[0]
    except IndexError:
        print('No block named "above-footer"')
    else:
        for textEl in elements:
            if 'h2' in str(textEl):
                # First we get <h2> text and if exist such element
                heading = textEl.text
                # 'n' variable is a count of found elements with same type
                for n, element in enumerate(elements, start=0):
                    websitesDict[linkProc]['footerHeading' + str(n)] = heading
                    break
            else:
                # First we get <p> text and if exist such element
                paragraph = textEl.text
                for n, element in enumerate(elements, start=0):
                    websitesDict[linkProc]['footerParagraph' + str(n)] = paragraph
                    break


def contentCreator():
    """
    This function add random and specific content do resultDict
    1: we need to check City and Category of website we need to create
    2: select by City and Category <title> and <meta>
    3: add random content to resultDict
    4: replace all keywords
    """
    print('Generating result...')
    # Add city, category and specific title & meta

    # resultDict['city'] = cityName
    # resultDict['mainCategory'] = 'CATEGORY'
    # resultDict['title'] = filterTitle(categoryList[1])
    # resultDict['meta'] = filterMeta(categoryList[1])
    # resultDict['headerHeading'] = filterHeaderHeading(categoryList[1])
    # resultDict['headerParagraph'] = filterHeaderParagraph(categoryList[1])
    # if random.choice([True, False]):
    #     createUnderHeader('underHeaderHeading')
    #     createUnderHeader('underHeaderParagraph')
    # else:
    #     pass
    createMainContainer()

    # testResult()
    # testWebsites()

"""
These lambda functions select title and meta from category
And return value to resultDict
"""

filterTitle = lambda title: headContent['title'][title]

filterMeta = lambda meta: headContent['meta'][meta]

"""
These lambda functions select heading and paragraph from headerContent
And return value to resultDict
"""

filterHeaderHeading = lambda headerHeading: headerContent['heading'][headerHeading]

filterHeaderParagraph = lambda headerHeading: headerContent['paragraph'][headerHeading]


def createUnderHeader(searchKey):
    """
    This function create random underHeader content
    And then add it to resultDict
    """
    result = []
    # Add all founded values by searchKey to result[]
    for key, value in websitesDict.items():
        for subKey in websitesDict.get(key, {}):
            if searchKey in str(subKey):
                result.append(websitesDict[key][subKey])
            else:
                pass
    # Catch empty array
    try:
        result[0]
    except IndexError:
        pass
    else:
        # Check to which key add new value
        if searchKey == 'underHeaderHeading':
            resultDict['mainUnderHeaderHeading'] = result[random.randint(0, len(result) - 1)]
        else:
            resultDict['mainUnderHeaderParagraph'] = result[random.randint(0, len(result) - 1)]


def createMainContainer():
    """
     This function create random mainContainer content
     And then add it to resultDict
     """

    searchKey = 'mainParagraph'

    result = []
    i = 0
    # Add all founded values by searchKey to result[]
    for key, value in websitesDict.items():
        for subKey in websitesDict.get(key, {}):
            if searchKey in str(subKey):
                print(websitesDict[key]['City'])
                # result.append(websitesDict[key][subKey])
            else:
                pass
    # TODO: Catch texts and headings which repeat
    #   Get current city and category to replace
    # Catch empty array
    # try:
    #     result[0]
    # except IndexError:
    #     pass
    # else:
    #     # Check to which key add new value
    #     if searchKey == 'underHeaderHeading':
    #         resultDict['mainUnderHeaderHeading'] = result[random.randint(0, len(result) - 1)]
    #     else:
    #         resultDict['mainUnderHeaderParagraph'] = result[random.randint(0, len(result) - 1)]


def testResult():
    for key, value in resultDict.items():
        print(str(key) + ' : ' + str(value) + '\n')


def testWebsites():
    for key, value in websitesDict.items():
        print(str(key) + ' : ' + str(value) + '\n')


if __name__ == '__main__':
    contentGenerator()
    contentCreator()
    # TODO: run in loop only contentCreator()
    #   To get all content only one time

    # CityList = [str(item) for item in input("Enter list of cities : ").split()]
    # for city in CityList:
    #     for category in CategoryList:
