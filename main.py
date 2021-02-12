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
mainCategory = 'Shopify'

cityCategory = 'Wordpress'
categoryList = ['Wordpress', 'Magento', 'Shopify', 'Development', 'Design']
headContent = {
    'Title':
    {
        'Design': '🥇 Web Design Agency in ' + cityName + '. Web designers in ' + cityName,
        'Dev': '🥇 Web Development Agency in ' + cityName + '. Web developers in ' + cityName,
        'Magento': '🥇 Magento Web Development & eCommerce consulting agency in ' + cityName,
        'Shopify': '🥇 Shopify Development Agency in ' + cityName + '. Web developers in ' + cityName,
        'WP': '🥇 WordPress & WooCommerce Development Agency in ' + cityName + '. Web developers in ' + cityName
    },
    'Meta':
    {
        'Design': 'Web design agency in ' + cityName + ' ✅ with full-stack front-end back-end developers in ' + cityName + '⚡',
        'Dev': 'Web development agency in ' + cityName + ' ✅ with full-stack frontend backend developers in ' + cityName + '⚡',
        'Magento': 'Magento agency in ' + cityName + ' ✅ with certified developers and solution specialists ready to start today. ⚡We design, develop and support.',
        'Shopify': 'Shopify agency in ' + cityName + ' ✅ with full-stack frontend backend developers in ' + cityName + '.⚡',
        'WP': 'WordPress & WooCommerce agency in ' + cityName + ' ✅ with full-stack frontend backend developers in ' + cityName + '. ⚡'
    }
}

# WRITE ALL STAGES OF GETTING AND COLLECTING


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
    if len(elements) != 0:
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
    else:
        print('No block named abovefooter')


def contentCreator():
    """
    This function add random and specific content do resultDict
    First: we need to check City and Category of website we need to create
    Second: select by City and Category <title> and <meta>
    Third: add random content to resultDict
    Fought: replace all keywords
    """
    print('Generating result...')
    # Add city, category and specific title & meta
    resultDict['city'] = cityName
    resultDict['mainCategory'] = mainCategory
    resultDict['title'] = filterTitle(categoryList[1])
    resultDict['meta'] = filterMeta(categoryList[1])
    # if random.choice([True, False]):
    #     resultDict['mainUnderHeaderHeading'] = createUnderHeader('underHeaderHeading'),
    #     resultDict['mainUnderHeaderParagraph'] = createUnderHeader('underHeaderParagraph')
    # else:
    #     pass

    for key, value in resultDict.items():
        print(str(key) + ' : ' + str(value) + '\n')


def filterTitle(categoryTitle):
    """
    This function select title from category
    for generating final dict of info
    """
    title = headContent['Title'][categoryTitle]
    return title


def filterMeta(categoryMeta):
    """
    This function select meta from category
    for generating final dict of info
    """
    meta = headContent['Meta'][categoryMeta]
    return meta

#
# def createUnderHeader():
#     """
#     This function create random underHeader content
#     And then add it to resultDict
#     """
#     searchKey = 'HeaderHeading'
#     result = []
#     try:
#         for key, value in websitesDict.items():
#             for subKey in websitesDict.get(key, {}):
#                 if searchKey in str(subKey):
#                     result.append(websitesDict[key][subKey])
#         return result[random.randint(0, len(result))]
#         print(result[random.randint(0, len(result))])
#     except NameError:
#         print('none')
#


if __name__ == '__main__':
    contentGenerator()
    # contentCreator()
    createUnderHeader()
    # CityList = [str(item) for item in input("Enter list of cities : ").split()]
    # for city in CityList:
    #     for category in CategoryList:


